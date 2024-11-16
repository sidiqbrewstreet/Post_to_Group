import requests, re, time, json, uuid, os, random
from itertools import zip_longest

class UploadGraphQL:
    def __init__(self, typ:int, cookie:str, GroupID:list, filename:list, captionz:list, timer:int) -> None:
        self.OK, self.Fail = 0, 0
        self.ses      = requests.Session()
        self.typ      = int(typ)
        self.cookie   = cookie
        self.timer    = timer
        self.headers  = {'Host': 'web.facebook.com','Sec-Ch-Ua-Platform': '"Windows"','Sec-Ch-Ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"','Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Prefers-Color-Scheme': 'dark','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','Sec-Ch-Ua-Platform-Version': '"15.0.0"','Accept': '*/*','Origin': 'https://web.facebook.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://web.facebook.com','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Priority': 'u=1, i'}
        for dir_path, caption in zip_longest(filename, captionz, fillvalue=None):
            if caption is None:
                caption = random.choice(captionz) if captionz else ''
            for IDGroup in GroupID:
                print('\rSedang Menyiapkan Data To > {}                                         '.format(str(IDGroup).split('|')[0]), end='')
                rtn_data = self.Getdata(IDGroup=str(IDGroup).split('|')[0])
                if rtn_data: self.GetIMG(dir_path, caption, str(IDGroup).split('|')[0])
                else:
                    self.Fail +=1
                    print('\r                                                                   ', end='')
                    print('\rFailed Upload To Group > {}                                                      '.format(str(IDGroup).split('|')[0]), end='')
                    print('\n')
                    print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
                    time.sleep(3)
                    self.jeda(self.timer, 'Upload Ulang')
        print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
        print('')

    def jeda(self, timers:int, msg:str):
        while timers > 0:
            print(f'\rMenunggu {msg} Dalam {timers} Detik...            ', end='')
            time.sleep(1)
            timers -= 1

    def Getdata(self, IDGroup):
        print('\rMengambil Data Group > {}                                                      '.format(IDGroup), end='')
        headers = self.headers.copy()
        headers.update({
            'X-Fb-Friendly-Name': 'ComposerStoryCreateMutation',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Upgrade-Insecure-Requests': '1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

        })
        response = self.ses.get('https://web.facebook.com/groups/{}'.format(IDGroup), cookies={'cookie': self.cookie}, headers=headers, allow_redirects=True).text.replace('\\','')
        self.sessionID = re.search(r'"UFI2Config",\[\],{"sessionID":"(.*?)"', str(response)).group(1)
        self.GroupID = re.search(r'"variables":{"groupID":"(\d+)"', str(response)).group(1)
        try:
            if   self.typ == 1: self.actorid = re.search(r'"name":"Peserta anonim","id":"(\d+)"', str(response)).group(1)
            elif self.typ == 2: self.actorid = re.search(r'"userId":(\d+)', str(response)).group(1)
            self.data = {
                'av': self.actorid,
                '__aaid': re.search(r'"__aaid":"(\d+)"', str(response)).group(1),
                '__user': re.search(r'"userId":(\d+)', str(response)).group(1),
                '__a': '1',
                '__req': '1f',
                '__hs': re.search(r'"haste_session":"(.*?)"', str(response)).group(1),
                'dpr': '1',
                '__ccg': re.search(r'"connectionClass":"(.*?)"', str(response)).group(1),
                '__rev': re.search(r'"rev":(\d+)', str(response)).group(1),
                '__hsi': re.search(r'"hsi":"(\d+)"', str(response)).group(1),
                '__comet_req': re.search(r'__comet_req=(\d+)&', str(response)).group(1),
                'fb_dtsg': re.search(r'"DTSGInitialData",\[\]\,{"token":"(.*?)"', str(response)).group(1),
                'jazoest': re.search(r'jazoest=(\d+)', str(response)).group(1),
                'lsd': re.search(r'"LSD",\[\]\,{"token":"(.*?)"', str(response)).group(1),
                '__spin_r': re.search(r'"__spin_r":(\d+)'  , str(response)).group(1),
                '__spin_b': re.search(r'"__spin_b":"(.*?)"', str(response)).group(1),
                '__spin_t': re.search(r'"__spin_t":(\d+)'  , str(response)).group(1),
            }
            return True
        except AttributeError: return False
        
    def GetIMG(self, dir_path, caption, GroupID):
        print('\rMembuka File Gambar > {}                                                                           '.format(os.path.basename(dir_path)), end='')
        file = {'file':(os.path.basename(dir_path), open(dir_path, 'rb'))}
        data = self.data.copy()
        data.update({
            'source':'8',
            'profile_id':data['__user'],
            'waterfallxapp':'comet',
            'farr':file['file']
        })
        pos = self.ses.post('https://upload.facebook.com/ajax/react_composer/attachments/photo/upload',data=data, files=file, cookies={'cookie':self.cookie}, allow_redirects=True).text
        self.id_foto = re.search('"photoID":"(.*?)"',str(pos)).group(1)
        if self.id_foto: self.Uploads(caption=caption, dir_path=dir_path)
        else: 
            self.Fail += 1
            print(f'\rGagal Mengambil Photo ID pada gambar {dir_path} - Group {GroupID}', end='')

    def var_input(self, caption) -> dict:
        var_output = {
            "composer_entry_point":"",
            "composer_source_surface":"group",
            "composer_type":"group",
            "logging":{"composer_session_id":self.sessionID},
            "source":"WWW",
            "message":{"ranges":[],"text":caption},
            "with_tags_ids":None,
            "inline_activities":[],
            "text_format_preset_id":"0",
            "attachments":[{"photo":{"id":self.id_foto}}],
            "navigation_data":{"attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1731467562591,717719,2361831622,,"},
            "tracking":[None],
            "event_share_metadata":{"surface":"newsfeed"},
            "audience":{"to_id":self.GroupID},
            "actor_id":self.actorid,
            "client_mutation_id":"1"}
        
        #---> 1 (Anonim) <> 2 (Biasa)
        if   self.typ == 1:
            var_output.update({"composer_entry_point":"publisher_bar_anonymous_author","ask_admin_to_post_for_user":{"is_asking_admin_to_post":True}})
            self.doc_id = '8884031438327075'
        elif self.typ == 2:
            var_output.update({"composer_entry_point":"inline_composer"})
            self.doc_id = '8667201500060239'
        return var_output
    
    def Uploads(self, caption, dir_path):
        print('\rMengupload File Gambar {} To > {}                                              '.format(os.path.basename(dir_path), self.GroupID), end='')
        data = self.data.copy()
        data.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
            'variables': json.dumps({
                "input": self.var_input(caption),
                "feedLocation":"GROUP",
                "feedbackSource":0,
                "focusCommentID":None,
                "gridMediaWidth":None,
                "groupID":None,
                "scale":1,
                "privacySelectorRenderLocation":"COMET_STREAM",
                "checkPhotosToReelsUpsellEligibility":False,
                "renderLocation":"group",
                "useDefaultActor":False,
                "inviteShortLinkKey":None,
                "isFeed":False,
                "isFundraiser":False,
                "isFunFactPost":False,
                "isGroup":True,
                "isEvent":False,
                "isTimeline":False,
                "isSocialLearning":False,
                "isPageNewsFeed":False,
                "isProfileReviews":False,
                "isWorkSharedDraft":False,
                "hashtag":None,
                "canUserManageOffers":False,
                "__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":True,
                "__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":False,
                "__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":False,
                "__relay_internal__pv__IsWorkUserrelayprovider":False,
                "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,
                "__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":False,
                "__relay_internal__pv__IsMergQAPollsrelayprovider":False,
                "__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":False,
                "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":True,
                "__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":False,
                "__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":False
            }),
            'server_timestamps': 'true',
            'doc_id': self.doc_id,
        })
        response = self.ses.post('https://web.facebook.com/api/graphql/', cookies={'cookie': self.cookie}, headers=self.headers, data=data, allow_redirects=True).text.replace('\\', '')
        try:
            match = re.findall(r'"url":"(.*?)"', str(response))
            self.OK +=1
            print('\r', end='')
            print('Link Group :', match[1])
            print('Link Post  :', match[3])
            print('')
            print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
            time.sleep(3)
            self.jeda(self.timer, 'Upload Ulang')
        except IndexError:
            self.Fail +=1
            print('\r                                                               ', end='')
            print('\rFailed Upload To Group > {}                                                  '.format(self.GroupID), end='')
            print('\n')
            print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
            time.sleep(3)
            self.jeda(self.timer, 'Upload Ulang')

class Share:
    def __init__(self, cookies:str, url:list, caption:list, IDGroup:list, timer:int):
        self.OK, self.Fail = 0, 0
        self.ses = requests.Session()
        self.cookie  = cookies
        self.headers = {'accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','priority': 'u=1, i','referer': 'https://web.facebook.com/profile.php?id=100068325679385','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.117", "Google Chrome";v="130.0.6723.117", "Not?A_Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','x-asbd-id': '129477','x-fb-friendly-name': 'ComposerStoryCreateMutation','x-fb-lsd': ''}
        for link, captions, GroupID in zip_longest(url, caption, IDGroup):
            self.GetData(urlx=link)
            self.ShareToGroup(caption=captions, GroupID=str(GroupID).split('|')[0])
            print('')
            print('\rSukses =-{} Gagal =-{}                 '.format(self.OK, self.Fail))
            time.sleep(3)
            self.jeda(timer, 'Membagikan Ulang')
        print('\rSukses Membagikan {} Postingan\nGagal Membagikan  {} Postingan                 '.format(self.OK, self.Fail))

    def jeda(self, timers:int, msg:str):
        while timers > 0:
            print(f'\rMenunggu {msg} Dalam {timers} Detik...            ', end='')
            time.sleep(1)
            timers -= 1

    def GetData(self, urlx):
        headers  = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','cookie': self.cookie,'dpr': '1.5','priority': 'u=0, i','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.117", "Google Chrome";v="130.0.6723.117", "Not?A_Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','viewport-width': '641',}
        response = self.ses.get(urlx, headers=headers).text.replace('\\','')
        if '?fbid=' in urlx:
            print('\rMengambil Data             ', end='')
            self.fbid = re.search(r'fbid=(\d+)', str(urlx)).group(1)
            self.legacy_story_hideable_id = re.search(r'"legacy_story_hideable_id":"(\d+)"', str(response)).group(1)
            self.data = {'av': re.search(r'"actorID":"(\d+)"', str(response)).group(1),'__aaid': '0','__user': re.search(r'"actorID":"(\d+)"', str(response)).group(1),'__a': '1','__req': '1t','__hs': re.search(r'"haste_session":"(.*?)"', str(response)).group(1),'dpr': '1','__ccg': re.search(r'"connectionClass":"(.*?)"', str(response)).group(1),'__rev': re.search(r'"rev":(\d+)', str(response)).group(1),'__hsi': re.search(r'"hsi":"(\d+)"', str(response)).group(1),'__comet_req': re.search(r'__comet_req=(\d+)&', str(response)).group(1),'fb_dtsg': re.search(r'inputs":\[\{"name":"fb_dtsg","value":"(.*?)"', str(response)).group(1),'jazoest': re.search(r'"name":"jazoest","value":"(\d+)"', str(response)).group(1),'lsd': re.search(r'"LSD",\[\]\,{"token":"(.*?)"', str(response)).group(1),'__spin_r': re.search(r'"__spin_r":(\d+)'  , str(response)).group(1),'__spin_b': re.search(r'"__spin_b":"(.*?)"', str(response)).group(1),'__spin_t': re.search(r'"__spin_t":(\d+)'  , str(response)).group(1)}
        else:
            print('\rRotate Url                 ', end='')
            url = re.findall(r'"url":"(.*?)"', str(response))
            self.url = [i for i in url if 'fbid=' in i and '&type=' not in i]
            self.GetData(self.url)
        
    def ShareToGroup(self, caption, GroupID):
        print('\rStart Share Post {} To {}           '.format(self.fbid, GroupID), end='')
        self.message = {"ranges":[],"text":caption}
        if isinstance(self.data, dict):
            self.data.update({
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'ComposerStoryCreateMutation',
                'variables': json.dumps({
                    "input":{
                        "composer_entry_point":"inline_composer",
                        "composer_source_surface":"group",
                        "composer_type":"group",
                        "logging":{"composer_session_id":str(uuid.uuid4())},
                        "source":"WWW",
                        "is_tracking_encrypted":True,
                        "tracking":[None],
                        "message":self.message,
                        "with_tags_ids":None,
                        "inline_activities":[],
                        "text_format_preset_id":"0",
                        "attachments":[{"link":{"share_scrape_data":json.dumps({"share_type":22,"share_params":[int(self.legacy_story_hideable_id)]})}}],
                        "navigation_data":{"attribution_id_v2":"CometPhotoRoot.react,comet.mediaviewer.photo,via_cold_start,,,,,"},"event_share_metadata":{"surface":"newsfeed"},"audience":{"to_id":GroupID},
                        "actor_id":self.data['av'],
                        "client_mutation_id":"1"
                    },
                    "feedLocation":"GROUP",
                    "feedbackSource":0,
                    "focusCommentID":None,
                    "gridMediaWidth":None,
                    "groupID":None,
                    "scale":1,
                    "privacySelectorRenderLocation":"COMET_STREAM",
                    "checkPhotosToReelsUpsellEligibility":False,
                    "renderLocation":"group",
                    "useDefaultActor":False,
                    "inviteShortLinkKey":None,
                    "isFeed":False,
                    "isFundraiser":False,
                    "isFunFactPost":False,
                    "isGroup":True,
                    "isEvent":False,
                    "isTimeline":False,
                    "isSocialLearning":False,
                    "isPageNewsFeed":False,
                    "isProfileReviews":False,
                    "isWorkSharedDraft":False,
                    "hashtag":None,
                    "canUserManageOffers":False,
                    "__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":True,
                    "__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":False,
                    "__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":False,
                    "__relay_internal__pv__IsWorkUserrelayprovider":False,
                    "__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,
                    "__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":False,
                    "__relay_internal__pv__IsMergQAPollsrelayprovider":False,
                    "__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":False,
                    "__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":True,
                    "__relay_internal__pv__EventCometCardImage_prefetchEventImagerelayprovider":False,
                    "__relay_internal__pv__GHLShouldChangeSponsoredAuctionDistanceFieldNamerelayprovider":True
                }),
                'server_timestamps': 'true',
                'doc_id': '8810532655635415',
            })

            response = self.ses.post('https://web.facebook.com/api/graphql/', cookies={'cookie': self.cookie}, headers=self.headers.update({'x-fb-lsd': self.data['lsd']}), data=self.data).text
            print(response)
            # if caption in str(response):
            #     self.OK +=1
            #     print('\rURL Post : {}                              '.format(re.search(r'"accessibility_caption":"Keterangan foto tidak tersedia.","url":"(.*?)"', str(response.replace('\\',''))).group(1)))
            #     print('')
            # else:
            #     self.Fail +=1
            #     print('\rGagal Membagikan Post {} To > {}           '.format(self.fbid, GroupID))
            #     print('')