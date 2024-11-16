import requests, os, sys, re, time
def clear(): os.system('cls' if 'win' in sys.platform.lower() else 'clear')

def Author():
    print('                                                         ')
    print(' ____ ___         __                     ___             ') 
    print('|    |   \______ |  |   _________     __| _/___________  ')
    print('|    |   /\____ \|  |  /  _ \__  \   / __ |/ __ \_  __ \ ')
    print('|    |  / |  |_> >  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/ ')
    print('|______/  |   __/|____/\____(____  /\____ |\___  >__|    ')
    print('          |__|                   \/      \/    \/        ')
    print('               Coded BY SIDIQ BREWSTREET                 ')
    print('                                                         ')

def Relogin():
    clear()
    Author()
    try:
        cookie = input('Masukkan Cookies : ')
        open('Login/cookie.json','w', encoding='utf-8').write(cookie)
        return(checkcookie())
    except KeyboardInterrupt: exit()

def checkcookie():
    try:
        cookie = open('Login/cookie.json','r').read()
        return(getinfo(cookie))
    except Exception as e:
        print('Cookies Invalid!')
        time.sleep(3)
        return(Relogin())
    except KeyboardInterrupt: exit()

def getinfo(cookie, types='Normal'):
    ses = requests.Session()
    if 'Normal' in types:
        try:
            req1 = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie': cookie},allow_redirects=True).text
            nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
            req2 = ses.get(nek1,cookies={'cookie': cookie},allow_redirects=True).text
            tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
            req  = ses.get(f'https://graph.facebook.com/me?fields=name,id&access_token={tok}',cookies={'cookie': cookie}).text
            name = re.search('"name":"(.*?)"',str(req)).group(1)
            user = re.search('"id":"(.*?)"'  ,str(req)).group(1)
            return(Print_Results(name=name, user=user))
        except requests.exceptions.ConnectionError: print('\rKoneksi Bermasalah', end='');exit()
    else:
        try:
            req1 = ses.get('https://www.facebook.com/adsmanager/manage/campaigns',cookies={'cookie': cookie},allow_redirects=True).text
            nek1 = re.search('window\.location\.replace\("(.*?)"\)',str(req1)).group(1).replace('\\','')
            req2 = ses.get(nek1,cookies={'cookie': cookie},allow_redirects=True).text
            tok  = re.search('accessToken="(.*?)"',str(req2)).group(1)
            req  = ses.get(f'https://graph.facebook.com/me?fields=name,id&access_token={tok}',cookies={'cookie': cookie}).text
            name = re.search('"name":"(.*?)"',str(req)).group(1)
            user = re.search('"id":"(.*?)"'  ,str(req)).group(1)
            return(name)
        except AttributeError: return False

def Print_Results(name, user):
    clear()
    Author()
    print('                --- Selamat Datang ---   ')
    print('                                         ')
    print('                  Nama :', name           )
    print('                  ID   :', user           )
    print('                                         ')
    return True