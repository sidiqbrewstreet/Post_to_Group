import requests, re, json, random, time

rand_int = lambda min=0, max=100 : str(random.randint(min, max))

DefaultUAWindows   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
HeadersGetWindows  = lambda i=DefaultUAWindows : {'Host':'business.facebook.com','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9, id-ID,id;q=0.8','Cache-Control':'max-age=0','Dpr':'2','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Ch-Ua-Model':'','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','Priority':'u=0, i','User-Agent':i}

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

class GraphQL:
    def __init__(self, cookies:str, IDGroup:list, types:int, timers:int):
        self.OK, self.Fail = 0, 0
        self.ses = requests.Session()
        self.types = int(types)
        self.cookies = {'cookie': cookies}
        self.c_user  = re.search(r'c_user=(\d+)', str(self.cookies)).group(1)
        self.headersPost = {'accept': '*/*','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','priority': 'u=1, i','referer': 'https://web.facebook.com','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '','sec-ch-ua-full-version-list': '','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': '','x-asbd-id': '129477','x-fb-friendly-name': 'GroupCometLeaveForumMutation','x-fb-lsd': ''}
        self.headersGet = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control': 'max-age=0','dpr': '1.5','priority': 'u=0, i','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '','sec-ch-ua-full-version-list': '','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': '','viewport-width': '619'}
        head = Useragents()    
        self.data, self.app_id = self.GetData(head=head)
        try:
            for x in IDGroup:
                if   self.types == 1:
                    print('\rMencoba Bergabung Group {}     '.format(x), end='')
                    results = self.JoinGroup(data=self.data, GroupID=x, app_id=self.app_id, head=head)
                elif self.types == 2:
                    GroupID = str(x).split('|')[0]
                    print('\rMencoba Leave Group {}     '.format(GroupID), end='')
                    results = self.LeaveGroup(data=self.data, GroupID=GroupID, head=head)
                if results:
                    self.OK +=1
                    print('')
                    print('')
                else:
                    self.Fail +=1
                    print('')
                    print('')
                print('\rSukses =-{} Gagal =-{}   '.format(self.OK, self.Fail), end='')
                time.sleep(5)
                self.jeda(timers, 'Mengulang')
            self.Print_results()
        except KeyboardInterrupt: self.Print_results()
        
    def Print_results(self):
        if self.types == 1:
            print('\rBerhasil Bergabung {} Group         '.format(self.OK), end='')            
            print('')
            print('\rGagal Bergabung {} Group        '.format(self.Fail), end='')
        elif self.types == 2:
            print('\rBerhasil Leave {} Group            '.format(self.OK), end='')
            print('')
            print('\rGagal Leave {} Group       '.format(self.Fail), end='')
        print('')

    def jeda(self, timers:int, msg:str):
        while int(timers) > 0:
            print(f'\rMenunggu {msg} Dalam {timers} Detik...  ', end='')
            time.sleep(1)
            timers -= 1

    def GetData(self, head:dict):
        req = self.ses.get('https://web.facebook.com', headers=self.headersGet.update({'sec-ch-ua': head['sec-ch-ua'], 'sec-ch-ua-full-version-list': head['sec-ch-ua-full-version-list'], 'user-agent': head['user-agent']}), cookies=self.cookies, allow_redirects=True).text.replace('\\','')
        try:
            av = re.search(r'"actorID":"(.*?)"',str(req)).group(1)
            __user = av
            __a = '1'
            __hs = re.search(r'"haste_session":"(.*?)"',str(req)).group(1)
            __ccg = re.search(r'"connectionClass":"(.*?)"',str(req)).group(1)
            __rev = re.search(r'"__spin_r":(.*?),',str(req)).group(1)
            __spin_r = __rev
            __spin_b = re.search(r'"__spin_b":"(.*?)"',str(req)).group(1)
            __spin_t = re.search(r'"__spin_t":(.*?),',str(req)).group(1)
            __hsi = re.search(r'"hsi":"(.*?)"',str(req)).group(1)
            fb_dtsg = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
            jazoest = re.search(r'jazoest=(.*?)"',str(req)).group(1)
            lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
            Data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
            app_id = re.search(r'"APP_ID":"(\d+)"', str(req)).group(1)
            return(Data, app_id)
        except Exception as e: return({})

    def JoinGroup(self, data:dict, GroupID:str, app_id:str, head:dict):
        data.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': json.dumps({
                "feedType":"DISCUSSION",
                "groupID":GroupID,
                "input":{
                    "action_source":"GROUP_MALL",
                    "attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,unexpected,1732547361934,306528,2361831622,,",
                    "group_id":GroupID,
                    "group_share_tracking_params":{
                        "app_id":app_id,
                        "exp_id":"null","is_from_share":False
                    },
                    "actor_id":self.c_user,
                    "client_mutation_id":"2"
                },
                "inviteShortLinkKey":None,
                "isChainingRecommendationUnit":False,
                "scale":1,
                "source":"GROUP_MALL",
                "renderLocation":"group_mall",
                "__relay_internal__pv__GroupsCometRelatedGroupsDataSourcerelayprovider":True,
                "__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False
            }),
            'server_timestamps': 'true',
            'doc_id': '8358751344247950',
            'fb_api_analytics_tags': ["qpl_active_flow_ids=431626709"]
        })
        headers = self.headersPost.copy()
        headers.update({'sec-ch-ua': head['sec-ch-ua'], 'sec-ch-ua-full-version-list': head['sec-ch-ua-full-version-list'], 'user-agent': head['user-agent'], 'x-fb-lsd': data['lsd']})
        response = self.ses.post('https://web.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data).json()['data']['group_request_to_join']['group']
        if response['viewer_join_state'] == "MEMBER":
            print('\rBerhasil Bergabung Ke Group {}  '.format(response['id']), end='')
            return True
        else:
            print('\rGagal Bergabung Ke Group {}     '.format(response['id']), end='')
            return False

    def LeaveGroup(self, data:dict, GroupID:str, head:dict):
        data.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometLeaveForumMutation',
            'variables': json.dumps({
                "input":{
                    "attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1732547262870,522472,2361831622,,",
                    "group_id":GroupID,
                    "actor_id":self.c_user,
                    "client_mutation_id":"1"
                },
                "inviteShortLinkKey":None,
                "isChainingRecommendationUnit":False,
                "ordering":["viewer_added"],
                "scale":1,
                "groupID":GroupID,
                "__relay_internal__pv__GroupsCometRelatedGroupsDataSourcerelayprovider":True,
                "__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":False
            }),
            'server_timestamps': 'true',
            'doc_id': '27485246481118934',
        })
        headers = self.headersPost.copy()
        headers.update({'sec-ch-ua': head['sec-ch-ua'], 'sec-ch-ua-full-version-list': head['sec-ch-ua-full-version-list'], 'user-agent': head['user-agent'], 'x-fb-lsd': data['lsd']})
        response = self.ses.post('https://web.facebook.com/api/graphql/', cookies=self.cookies, headers=headers, data=data).json()['data']['leave_forum_group']['group']
        if response['viewer_join_state'] == "CAN_JOIN":
            print('\rBerhasil Keluar Dari Group {}  '.format(response['name']), end='')
            return True
        else:
            print('\rGagal Keluar Dari Group {}     '.format(response['name']), end='')
            return False