import requests, re, time, json, uuid, os, random
from itertools import zip_longest

rand_int = lambda min=0, max=100 : str(random.randint(min, max))

def Useragents():
    ver1  = '10_%s_%s'%(str(rand_int(8,13)), str(rand_int(4,15)))
    ver2  = '10_%s'%(str(rand_int(4,13)))
    win   = 'Windows NT %s; Win64; %s'%(str(random.choice(['12.0','11.0','10.0','9.0','9.1','9.2','9.3','9.5','8.0','8.1','8.2','8.3','8.4','8.5'])), str(random.choice(['x64','WOW64'])))
    osver = 'Macintosh; Intel Mac OS X %s'%(str(random.choice([ver1, ver2])))
    linux = 'X11; Linux x86_64'
    type  = str(random.choice([win, osver, linux]))
    vs    = str(random.choice(['124.0.6367.54','124.0.6367.54','123.0.6312.121','123.0.6312.120','123.0.6312.119','123.0.6312.118','123.0.6312.99','123.0.6312.81','123.0.6312.80','123.0.6312.41','123.0.6312.41','123.0.6312.40','122.0.6261.120','122.0.6261.119','122.0.6261.119','122.0.6261.106','122.0.6261.106','122.0.6261.105','122.0.6261.91','122.0.6261.90','122.0.6261.90','122.0.6261.65','122.0.6261.64','122.0.6261.43','121.0.6167.180','121.0.6167.178','121.0.6167.165','121.0.6167.164','121.0.6167.164','121.0.6167.144','121.0.6167.143','121.0.6167.101','120.0.6099.230','120.0.6099.210','120.0.6099.194','120.0.6099.193','120.0.6099.145','120.0.6099.144','120.0.6099.144','120.0.6099.116','120.0.6099.116','120.0.6099.115','120.0.6099.44','120.0.6099.43','119.0.6045.194','119.0.6045.193','119.0.6045.164','119.0.6045.163','119.0.6045.134','119.0.6045.134','119.0.6045.66','119.0.6045.53','118.0.5993.112','118.0.5993.111','118.0.5993.80','118.0.5993.65','118.0.5993.48','117.0.5938.154','117.0.5938.141','117.0.5938.140','117.0.5938.61','117.0.5938.61','117.0.5938.60','116.0.5845.172','116.0.5845.164','116.0.5845.163','116.0.5845.114','116.0.5845.92','115.0.5790.136','114.0.5735.60','114.0.5735.53','113.0.5672.77','113.0.5672.76','112.0.5615.136','112.0.5615.136','112.0.5615.101','112.0.5615.100','112.0.5615.48','111.0.5563.116','111.0.5563.115','111.0.5563.58','111.0.5563.49','110.0.5481.154','110.0.5481.153','110.0.5481.65','110.0.5481.64','110.0.5481.63','110.0.5481.61','109.0.5414.118','109.0.5414.117','109.0.5414.86','108.0.5359.128','108.0.5359.61','107.0.5304.141','107.0.5304.105','107.0.5304.91','106.0.5249.126','106.0.5249.79','106.0.5249.65','105.0.5195.136','105.0.5195.124','105.0.5195.79','105.0.5195.77','105.0.5195.68','104.0.5112.97','104.0.5112.69','103.0.5060.129','103.0.5060.71','103.0.5060.70','103.0.5060.53','102.0.5005.125','102.0.5005.99','102.0.5005.78','102.0.5005.59','102.0.5005.59','101.0.4951.61','101.0.4951.41','100.0.4896.127','100.0.4896.88','100.0.4896.79','100.0.4896.58','99.0.4844.73','99.0.4844.58','99.0.4844.48','98.0.4758.101','98.0.4758.87','97.0.4692.98','97.0.4692.87','97.0.4692.70','96.0.4664.104','96.0.4664.92','95.0.4638.74','95.0.4638.74','95.0.4638.74','95.0.4638.50','95.0.4638.50','95.0.4638.50','95.0.4638.50','95.0.4638.50','94.0.4606.85','94.0.4606.85','94.0.4606.85','94.0.4606.85','94.0.4606.85','94.0.4606.85','94.0.4606.80','94.0.4606.71','94.0.4606.71','94.0.4606.71','94.0.4606.71','94.0.4606.71','94.0.4606.61','94.0.4606.61','94.0.4606.61','94.0.4606.61','94.0.4606.61','94.0.4606.50','94.0.4606.50','94.0.4606.50','94.0.4606.50','93.0.4577.82','93.0.4577.82','93.0.4577.82','93.0.4577.82','93.0.4577.82','93.0.4577.62','93.0.4577.62','93.0.4577.62','93.0.4577.62','93.0.4577.62','93.0.4577.62','92.0.4515.166','92.0.4515.166','92.0.4515.166','92.0.4515.166','92.0.4515.166','92.0.4515.159','92.0.4515.159','92.0.4515.159','92.0.4515.159','92.0.4515.159','92.0.4515.159','92.0.4515.131','92.0.4515.131','92.0.4515.131','92.0.4515.131','92.0.4515.131','92.0.4515.115','92.0.4515.115','92.0.4515.115','92.0.4515.115','92.0.4515.105','92.0.4515.105','91.0.4472.164','91.0.4472.134','91.0.4472.120','91.0.4472.114','91.0.4472.101','91.0.4472.88','91.0.4472.77','91.0.4472.77','91.0.4472.16','90.0.4430.210','90.0.4430.210','90.0.4430.210','90.0.4430.210','90.0.4430.210','90.0.4430.210','90.0.4430.91','90.0.4430.91','90.0.4430.91','90.0.4430.82','90.0.4430.82','90.0.4430.82','90.0.4430.66','90.0.4430.66','90.0.4430.66','89.0.4389.105','89.0.4389.105','89.0.4389.105','89.0.4389.90','89.0.4389.90','89.0.4389.90','89.0.4389.86','89.0.4389.86','89.0.4389.86','89.0.4389.72','89.0.4389.72','88.0.4324.181','88.0.4324.181','88.0.4324.181','88.0.4324.155','88.0.4324.155','88.0.4324.152','88.0.4324.152','88.0.4324.152','88.0.4324.141','88.0.4324.141','88.0.4324.141','88.0.4324.93','88.0.4324.93','88.0.4324.93','88.0.4324.93','87.0.4280.141','87.0.4280.141','87.0.4280.141','87.0.4280.141','87.0.4280.101','87.0.4280.101','87.0.4280.101','87.0.4280.101','87.0.4280.86','87.0.4280.86','87.0.4280.86','87.0.4280.86','87.0.4280.86','87.0.4280.66','87.0.4280.66','87.0.4280.66','86.0.4240.198','86.0.4240.198','86.0.4240.185','86.0.4240.185','86.0.4240.114','86.0.4240.114','86.0.4240.110','86.0.4240.110','86.0.4240.110','86.0.4240.99','86.0.4240.99','86.0.4240.99','86.0.4240.75','86.0.4240.75','85.0.4183.127','85.0.4183.127','85.0.4183.127','85.0.4183.127','85.0.4183.101','85.0.4183.101','85.0.4183.101','85.0.4183.101','85.0.4183.81','85.0.4183.81','85.0.4183.81']))
    agent = f'Mozilla/5.0 ({type}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{vs} Safari/537.36'
    sec_ua = f'"Chromium";v="{vs}", "Google Chrome";v="{vs}", "Not?A_Brand";v="99"'
    vrs_lst = f'"Chromium";v="{vs}", "Google Chrome";v="{vs}", "Not?A_Brand";v="99.0.0.0"'
    head = {'user-agent': agent,'sec-ch-ua' : sec_ua,'sec-ch-ua-full-version-list': vrs_lst}
    return head

class UploadGraphQL:
    def __init__(self, typ:int, cookie:str, GroupID:list, filename:list, captionz:list, timer:int) -> None:
        self.OK, self.Fail = 0, 0
        self.ses      = requests.Session()
        self.typ      = int(typ)
        self.cookie   = cookie
        for dir_path, caption in zip_longest(filename, captionz, fillvalue=None):
            if caption is None:
                caption = random.choice(captionz) if captionz else ''
            for IDGroup in GroupID:
                head = Useragents()
                self.headers    = {'Host': 'web.facebook.com','Sec-Ch-Ua-Platform': '"Windows"','Sec-Ch-Ua': '{}'.format(head['sec-ch-ua']),'Sec-Ch-Ua-Mobile': '?0','Sec-Ch-Prefers-Color-Scheme': 'dark','User-Agent': '{}'.format(head['user-agent']),'Sec-Ch-Ua-Platform-Version': '"15.0.0"','Accept': '*/*','Origin': 'https://web.facebook.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://web.facebook.com','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Priority': 'u=1, i'}
                print('\rSedang Menyiapkan Data To > {}                                         '.format(str(IDGroup).split('|')[0]), end='')
                rtn_data = self.Getdata(IDGroup=str(IDGroup).split('|')[0])
                if rtn_data:
                    rtn_foto_id = self.GetIMG(dir_path, str(IDGroup).split('|')[0])
                    if rtn_foto_id:
                        rtn_upload = self.Uploads(caption=caption, dir_path=dir_path)
                        if rtn_upload:
                            if self.typ == 1: link_post = rtn_upload[3]
                            else: link_post = rtn_upload[0]
                            self.OK +=1
                            print('\r', end='')
                            print('URL Post  :', link_post)
                            print('URL Group :', rtn_upload[1])
                            print('')
                            print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')

                        else:
                            self.Fail +=1
                            print('\r                                                               ', end='')
                            print('\rFailed Upload To Group > {}                '.format(self.GroupID), end='')
                            print('\n')
                            print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
                    else:
                        self.Fail +=1
                        print('\r                                                               ', end='')
                        print('\rFailed Upload To Group > {}                '.format(self.GroupID), end='')
                        print('\n')
                        print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
                else:
                    self.Fail +=1
                    print('\r                           ', end='')
                    print('\rFailed Upload To Group > {}                                                      '.format(str(IDGroup).split('|')[0]), end='')
                    print('\n')
                    print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
                    
                time.sleep(3)
                self.jeda(int(timer), 'Upload Ulang')
        print('\rSukses Upload =-{} Gagal Upload =-{}       '.format(self.OK, self.Fail), end='')
        print('')

    def jeda(self, timers:int, msg:str):
        while int(timers) > 0:
            print(f'\rMenunggu {msg} Dalam {timers} Detik...            ', end='')
            time.sleep(1)
            timers -= 1

    def Getdata(self, IDGroup):
        print('\rMengambil Data Group > {}              '.format(IDGroup), end='')
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
        try:
            self.sessionID = re.search(r'"UFI2Config",\[\],{"sessionID":"(.*?)"', str(response)).group(1)
            self.GroupID = re.search(r'"variables":{"groupID":"(\d+)"', str(response)).group(1)
            if   self.typ == 1: self.actorid = re.search(r'"__typename":"GroupAnonAuthorProfile","id":"(\d+)"', str(response)).group(1)
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
        
    def GetIMG(self, dir_path, GroupID):
        print('\rMembuka File Gambar > {}               '.format(os.path.basename(dir_path)), end='')
        file = {'file':(os.path.basename(dir_path), open(dir_path, 'rb'))}
        data = self.data.copy()
        data.update({
            'source':'8',
            'profile_id':data['__user'],
            'waterfallxapp':'comet',
            'farr':file['file']
        })
        pos = self.ses.post('https://upload.facebook.com/ajax/react_composer/attachments/photo/upload',data=data, files=file, cookies={'cookie':self.cookie}, allow_redirects=True).text
        try:
            self.id_foto = re.search('"photoID":"(.*?)"',str(pos)).group(1)
            if self.id_foto: return True
            else: 
                self.Fail += 1
                print(f'\rGagal Mengambil Photo ID pada gambar {dir_path} - Group {GroupID}', end='')
                return False
        except AttributeError: return False

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
        print('\rMengupload File Gambar {} To > {}              '.format(os.path.basename(dir_path), self.GroupID), end='')
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
        match = re.findall(r'"url":"(.*?)"', str(response))
        if not match: return False
        else: return match

class Share:
    def __init__(self, cookies:str, url:list, caption:list, IDGroup:list, timer:int):
        self.stop_all = False
        self.OK, self.Fail = 0, 0
        self.ses = requests.Session()
        self.cookie  = cookies
        self.head = {'accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','priority': 'u=1, i','referer': 'https://web.facebook.com/profile.php?id={}'.format(re.search(r'c_user=(\d+)', str(self.cookie)).group(1)),'sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '','sec-ch-ua-full-version-list': '','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': '','x-asbd-id': '129477','x-fb-friendly-name': 'ComposerStoryCreateMutation','x-fb-lsd': ''}
        for link, captions in zip_longest(url, caption):
            if self.stop_all: break
            else:
                if captions is None:
                    captions = random.choice(caption) if caption else ''
                for GroupID in IDGroup:
                    if self.stop_all: break
                    else:
                        head = Useragents()
                        self.headers = self.head.copy()
                        self.headers.update({'user-agent': head['user-agent'],'sec-ch-ua' : head['sec-ch-ua'],'sec-ch-ua-full-version-list': head['sec-ch-ua-full-version-list']})
                        getdata = self.GetData(urlx=link)
                        # if 'checkpoint' in getdata:
                        #     print('\rSepertinya Akun Anda Kena Checpoint Silahkan Periksa Akun Anda     ', end='')
                        #     # self.stop_all = True
                        #     break
                        if getdata:
                            share = self.ShareToGroup(caption=captions, GroupID=str(GroupID).split('|')[0])
                            # if 'checkpoint' in share:
                            #     print('\rSepertinya Akun Anda Kena Checpoint Silahkan Periksa Akun Anda     ', end='')
                            #     # self.stop_all = True
                            #     break
                            if share:
                                print('')
                            else:
                                print('\r                                                           ', end='')
                                print('\rGagal Share Postingan to > {}                  '.format(str(GroupID).split('|')[0]), end='')
                                print('')
                                print('')
                                self.Fail +=1
                        else: 
                            self.Fail +=1
                            print('\rGagal Mengambil Data                   ', end='')
                    print('\rSukses =-{} Gagal =-{}                 '.format(self.OK, self.Fail), end='')
                    time.sleep(3)
                    self.jeda(timer, 'Membagikan Ulang')
        print('\rSukses Membagikan =-{} Postingan             \nGagal  Membagikan =-{} Postingan                 '.format(self.OK, self.Fail))

    def jeda(self, timers:int, msg:str):
        while int(timers) > 0:
            print(f'\rMenunggu {msg} Dalam {timers} Detik...            ', end='')
            time.sleep(1)
            timers -= 1

    def Data(self):
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','dpr': '1.5','priority': 'u=0, i','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"','sec-ch-ua-full-version-list': '"Google Chrome";v="131.0.6778.86", "Chromium";v="131.0.6778.86", "Not_A Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36','viewport-width': '619'}
        response = self.ses.get('https://www.facebook.com/', headers=headers, cookies={'cookie': self.cookie}).text.replace('\\', '')
        self.data = {'av': re.search(r'"actorID":"(\d+)"', str(response)).group(1),'__aaid': '0','__user': re.search(r'"actorID":"(\d+)"', str(response)).group(1),'__a': '1','__req': '1t','__hs': re.search(r'"haste_session":"(.*?)"', str(response)).group(1),'dpr': '1','__ccg': re.search(r'"connectionClass":"(.*?)"', str(response)).group(1),'__rev': re.search(r'"rev":(\d+)', str(response)).group(1),'__hsi': re.search(r'"hsi":"(\d+)"', str(response)).group(1),'__comet_req': re.search(r'__comet_req=(\d+)&', str(response)).group(1),'fb_dtsg': re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(response)).group(1),'jazoest': re.search(r'jazoest=(\d+)', str(response)).group(1),'lsd': re.search(r'"LSD",\[\],{"token":"(.*?)"', str(response)).group(1),'__spin_r': re.search(r'"__spin_r":(\d+)', str(response)).group(1),'__spin_b': re.search(r'"__spin_b":"(.*?)"', str(response)).group(1),'__spin_t': re.search(r'"__spin_t":(\d+)'  , str(response)).group(1)}

    def GetData(self, urlx):
        headers  = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','dpr': '1.5','priority': 'u=0, i','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.117", "Google Chrome";v="130.0.6723.117", "Not?A_Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36','viewport-width': '641',}
        response = self.ses.get(urlx, headers=headers, cookies={'cookie': self.cookie}).text.replace('\\','')
        #if 'checkpoint' in response: return('checkpoint')
    
        try:
            print('\rMengambil Data                                     ', end='')
            self.legacy_story_hideable_id = re.search(r'"legacy_story_hideable_id":"(\d+)"', str(response)).group(1)
            self.fbid = str(self.legacy_story_hideable_id)
            self.Data()
            return True
        except requests.exceptions.ConnectionError:
            print('\rKoneksi Bermasalah Sedang Menghubungkan Kembali...         ', end='')
            time.sleep(7.5)
            print('\r                                                           ', end='')
            return(self.GetData(urlx))
        except Exception:
            print(response)
            print('')
            return False
        
    def ShareToGroup(self, caption, GroupID):
        print('\rStart Share Post {} To {}                              '.format(self.fbid, GroupID), end='')
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

            response = self.ses.post('https://web.facebook.com/api/graphql/', cookies={'cookie': self.cookie}, headers=self.headers.update({'x-fb-lsd': self.data['lsd']}), data=self.data).text.replace('\\','')
            try:
                self.OK +=1
                res = re.findall(r'"url":"(.*?)"', str(response))
                url_post, url_grop, postingn = res[0], res[1], res[3]
                print('\r                                                               ', end='')
                print('\rURL Post  :', url_post)
                print('URL Group :', url_grop)
                print('Postingan :', postingn)
                print('')
                return True
            except requests.exceptions.ConnectionError:
                print('\rKoneksi Bermasalah Sedang Menghubungkan Kembali            ', end='')
                time.sleep(7.5)
                print('\r                                                           ', end='')
                return(self.ShareToGroup(caption, GroupID))
            except Exception: return False
