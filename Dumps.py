import requests, re, json

class Dumps:
    def __init__(self, cookie:str):
        self.ses = requests.Session()
        self.ok, self.ids = 0, []
        self.cookies = cookie
        self.headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','priority': 'u=0, i','sec-ch-prefers-color-scheme': 'dark','sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.117", "Google Chrome";v="130.0.6723.117", "Not?A_Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

    def Dumps_ID_Group(self):
        response = self.ses.get('https://web.facebook.com/groups/joins/?nav_source=tab', cookies={'cookie': self.cookies}, headers=self.headers).text
        matches  = re.findall(r'"id":\s*"(\d+)",\s*"viewer_last_visited_time":\s*\d+,\s*"name":\s*"([^"]+)"', str(response))
        for group_id, group_name in matches:
            
            if group_id in self.ids: pass
            else:
                self.ok +=1
                self.ids.append(f'{group_id}|{group_name}')
                print(f"\rMengecek Group {self.ok}  ", end='')
        match = re.search(r'"end_cursor":"(.*?)","has_next_page":true}},"total_joined_groups":(\d+)', str(response))
        if match:
            end_cursor = match.group(1)
            self.GetData(response)
            self.LoopDumpsGroup(end_cursor)
        else: pass
        return self.ids
        
    def GetData(self, response:str):
        self.data = {
            'av': re.search(r'"userId":(\d+)', str(response)).group(1),
            '__aaid': '0',
            '__user': re.search(r'"userId":(\d+)', str(response)).group(1),
            '__a': '1',
            '__req': '1t',
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

    def LoopDumpsGroup(self, NextPage:str):
        self.data.update({
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupsCometAllJoinedGroupsSectionPaginationQuery',
            'variables': json.dumps({"count":20,"cursor":NextPage,"ordering":["integrity_signals"],"scale":1}),
            'server_timestamps': 'true',
            'doc_id': '6009728632468556',
        })

        response = self.ses.post('https://web.facebook.com/api/graphql/', cookies={'cookie': self.cookies}, headers=self.headers, data=self.data).json()
        parser = response['data']['viewer']['all_joined_groups']['tab_groups_list']
        for x in parser['edges']:
            group_id = x['node']['id']
            group_name = x['node']['name']
            if group_id in self.ids: pass
            else:
                self.ok +=1
                self.ids.append(f'{group_id}|{group_name}')
                print(f"\rMengumpulkan Group {self.ok}  ", end='')

        if parser['page_info']['end_cursor']:
            nextpages = parser['page_info']['end_cursor']
            self.LoopDumpsGroup(nextpages)
        else: print('\rTerdapat {} Group'.format(self.ok), end='')