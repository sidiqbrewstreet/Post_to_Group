from Login  import *
from Dumps  import *
from Upload import *
from Invite import *

class Menu:
    def __init__(self):
        self.dashboar()
    
    def dashboar(self):
        clear()
        Author()
        validasi = checkcookie()
        if validasi: self.MainMenu()
        else: exit('Login Gagal, Silahkan Login Dengan Cookies Fresh')
    
    def Folder_Menu(self):
        folder_path = input("\rMasukkan path folder (misal: Downloads/img) : ")
        if os.path.isdir(folder_path):
            files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            return files
        else:
            print("\rPath folder tidak ditemukan.                           ", end='')
            return(self.Folder_Menu())
    
    def Rotate_Cookie(self, type_cookie='Normal'):
        if 'Rotate' in type_cookie:
            cookie = input('\r\r[?] Masukan Cookie, [ENTER] Untuk Kembali : ')
            if not cookie: return (open('Login/cookie.json','r', encoding='utf-8').read())
            else:
                check_cookie = getinfo(cookie, 'Rotate')
                if check_cookie:
                    print('')
                    print('\rLogin Berhasil Sebagai {}      '.format(check_cookie), end='\n')
                    return cookie
                else:
                    print('\r\r\r\rLogin Gagal Kemungkinan Cookie Expired', end='')
                    time.sleep(3)
                    print('\r                                                          ')
                    return(self.Rotate_Cookie('Rotate'))
        else: pass

    def Setting_cookie(self):
        print('Apakah Ingin Mengunakan Cookie Lain ? (Y/T)')
        type_cookie = input('[?] Pilih (Y/T) : ').lower();print('')
        if   type_cookie in ['y']: self.cookie = self.Rotate_Cookie('Rotate');print('')
        elif type_cookie in ['t']: self.cookie = open('Login/cookie.json','r', encoding='utf-8').read()
        else: exit('Input Tidak Valid!')

    def MainMenu(self):
        try:
            print('[1] Upload Photo to Group')
            print('[2] Shared Photo to Group')
            print('[3] Joined to Group')
            print('[4] Leave to Group')
            print('[5] Logout Session')
            try: chose = input('[?] Pilih : ')
            except ValueError:
                print('')
                print('Input Harus Berupa Angka')
                clear()
                Author()
                self.MainMenu()
            print('')
            if not chose: exit('input Tidak Valid!')
            elif chose in ['1', '01']:
                self.Setting_cookie()
                print('Upload Sebagai Anonim (A) / Personal (P)')
                model = input('[?] Pilih [A / P] : ');print('')
                if   model in ['A', 'a', '2', '02']: typ = 1
                elif model in ['P', 'p', '1', '01']: typ = 2
                else: exit('Input Tidak Valid!')
                filename = self.Folder_Menu()
                print('')
                ctpn = input('Apakah Ingin Menggunakan Caption ? (Y / [ENTER]) : ');print('')
                if   ctpn.lower() in ['y']: 
                    print('Gunakan Koma (,) Jika Lebih Dari 1')
                    caption = input('[?] Masukan Caption : ').split(',');print('')
                elif ctpn.lower() in ['t'] or not ctpn: caption = []
                else: exit('Input Tidak Valid!')
                print('Atur Waktu Tunggu Dalam Detik')
                timers = input('[?] Delay : ');print('')
                if self.cookie is None: exit('\nCookie Tidak Ditemukan')
                else:
                    DM = Dumps(self.cookie)
                    list_id_group = DM.Dumps_ID_Group()
                    UploadGraphQL(typ=typ, cookie=self.cookie, GroupID=list_id_group, filename=filename, captionz=caption, timer=timers)

            elif chose in ['2', '02']: 
                self.Setting_cookie()
                print('Gunakan Koma (,) Jika Lebih Dari 1')
                url  = input('[?] Link Post : ').split(',');print('')
                ctpn = input('Apakah Ingin Menggunakan Caption ? (Y / [ENTER]) : ');print('')
                if   ctpn.lower() in ['y']: 
                    print('Gunakan Koma (,) Jika Lebih Dari 1')
                    caption = input('[?] Masukan Caption : ').split(',');print('')
                elif ctpn.lower() in ['t'] or not ctpn: caption = []
                else: exit('Input Tidak Valid!')
                print('Atur Waktu Tunggu Dalam Detik')
                timers = int(input('[?] Delay : '));print('')
                if self.cookie is None: exit('\nCookie Tidak Ditemukan')
                else:
                    DM = Dumps(self.cookie)
                    list_id_group = DM.Dumps_ID_Group()
                    Share(cookies=self.cookie, url=url, caption=caption, IDGroup=list_id_group, timer=timers)
            
            elif chose in ['3', '03', '4', '04']:
                self.Setting_cookie()
                print('Atur Waktu Tunggu Dalam Detik')
                timers = int(input('[?] Delay : '));print('')
                if chose in ['3', '03']:
                    types = 1
                    with open(r'GroupID/GroupID.txt', 'r', encoding='utf-8') as r:
                        GroupID = r.read().splitlines()
                        if not GroupID:
                            print('Isi File Kosong, Siahkan Isi ID Group nya Terlebih Dahulu')
                            exit('')
                        else: pass
                    r.close()
                elif chose in ['4', '04']:
                    types = 2
                    DM = Dumps(self.cookie)
                    GroupID = DM.Dumps_ID_Group()
                GraphQL(cookies=self.cookie, IDGroup=GroupID, types=types, timers=timers)

            elif chose in ['5', '05']:
                os.remove('Login/cookie.json')
                print('Logout Berhasil, Silahkan Login Kembali Dengan Cookies Fresh')
                exit('')
            else: exit('Input Tidak Valid!')
        except KeyboardInterrupt: exit()

if __name__ == '__main__':
    os.system('git pull')
    lo = Menu()
    