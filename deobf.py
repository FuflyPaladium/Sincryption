# Team Sincryption
# Founders : vaimpier , samay , cold , shark 
# Co-Founders : Aayush , Argatics
# Python programmming 


# ------imports 
import os 
import sys
try:
    import colorama
    import requests
    import bs4
except ImportError:
    os.system(\'pip install colorama\' if os.name==\'nt\' else \'pip install colorama\')
    os.system(\'pip install requests\' if os.name==\'nt\' else \'pip install requests\')
    os.system(\'pip install bs4\' if os.name==\'nt\' else \'pip install bs4\')
from colorama import Fore
from time import sleep
import requests
from bs4 import BeautifulSoup


#------colors 
r = "\\033[1;31m"
g = "\\033[1;32m"
y = "\\033[1;33m"
b = "\\033[1;34m"
d = "\\033[2;37m"
R = "\\033[1;41m"
Y = "\\033[1;43m"
B = "\\033[1;44m"
w = "\\033[1;37m"
g = "\\033[0;90m"
gg = "\\033[1;32m"
y = r


#-----------banner and logos 

logo = \'\'\'
    \\033[1;31m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97        \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97
    \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91        \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[0;90m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\\033[1;33m    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\033[1;33m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;33m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91           \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91
    \\033[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d           \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d
\'\'\'

def banner():
    print(logo)

def clear():
    os.system(\'cls\' if os.name==\'nt\' else \'clear\')

def space():
    print(\'\
\')


database_list = [\'sincrypt_argatics\',\'sincryptzork\',\'sincryptshark\',\'sincrypt_ace\',\'sincrypt.s3nu\',\'sincryptr4j\',\'sincrypt4drio\',\'sincrypt.s3nu\',\'sincryptx0\',\'sincryptzara\',\'sincryptveer\']

database_list2 = [
    \'sincryptm4dxt\',
    \'sincryptg0ku\',
    \'sincryptayush\',
    \'sincrypt_n1nja\',
    \'sincryptrew1sh\',
    \'sincryptr2dra\',
    \'sincryptr4drx\',
    \'sincryptxsl4shu\',
    \'sincryptrand0m\',
    \'sincryptdrag0n\',
    \'sincrypt.vdnt\',
    \'sincryptl0ve\',
    \'sincrypts3npa1\',
    \'sincryptpiyush\',
    \'sincryptk3n\',
    \'sincryptsn1p3r\',
    \'sincrypt.rahul\',
    \'sincryptxhisoka\',
    \'sincrypth4wk\',
    \'sincryptpriyanshu\',
    \'sincrypteagle\',
]

def madarchod(name):
    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+f"{name}")

def options():
    madarchod(\'[ 1 ] Check Username : \')
    madarchod(\'[ 2 ] About User :\')
    madarchod(\'[ 3 ] Update :\')
    madarchod(\'[ 4 ] Exit :\')

def front_final():
    clear()
    banner()
    space()
    options()
    space()

def _cls_front_():
    clear()
    banner()
    space()

front_final()

class Samay:
    project = \'Sincryption Panel !\'
    def __init__(self,_user_):
        self.data = _user_
    def functions(self):
        if self.data==1:
            _cls_front_()

            self.username = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Enter the Instagram Username : "+r)
            #
            
            url = \'https://www.instagram.com\'

            localmids = requests.get(url).cookies[\'mid\']
            localtoken = requests.get(url).cookies[\'csrftoken\']
            localigdidi = requests.get(url).cookies[\'ig_did\']


            cookies = {
                \'ig_did\': localigdidi,
                \'ig_nrcb\': \'1\',
                \'mid\': localmids,
                \'datr\': \'BL47YvvCmZh9a49mlTROe_R1\',
                \'ds_user_id\': \'237855618\',
                \'csrftoken\': localtoken,
                \'dpr\': \'1.25\',
                \'shbid\': \'"12935\\\\054237855618\\\\0541693755558:01f7bd94873a19cc89516f15a2c7cd52f8c1a70666fedb519473d266b6270fba2c0306b9"\',
                \'shbts\': \'"1662219558\\\\054237855618\\\\0541693755558:01f797ac5e7e7ce3a783864a712ce701daf645f0b53ec345daf7c1b10fa260c9dd4426dc"\',
                \'sessionid\': \'237855618%3AaTfU3dQmbnhBit%3A23%3AAYeXUTjBjMu7aqEViQMWFvAM9RYUldXW89hFYXcl0Q\',
                \'rur\': \'"VLL\\\\054237855618\\\\0541693755575:01f7f9d3e732fb5b95fd7436923c9153e8a46a8d70ac15448a4e229af0d9b0e8872fe46d"\',
            }

            headers = {
                \'authority\': \'www.instagram.com\',
                \'accept\': \'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\',
                \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',
                \'cache-control\': \'max-age=0\',
                # Requests sorts cookies= alphabetically
                # \'cookie\': \'ig_did=4552821A-91C2-4A0E-95DD-AAE0D34A7914; ig_nrcb=1; mid=YiTsfQALAAFciQQ2eE0cNnMgdXEK; datr=BL47YvvCmZh9a49mlTROe_R1; ds_user_id=237855618; csrftoken=TLyqyVhTxt9xXK8Q6HD5OqCG41APPHDO; dpr=1.25; shbid="12935\\\\054237855618\\\\0541693755558:01f7bd94873a19cc89516f15a2c7cd52f8c1a70666fedb519473d266b6270fba2c0306b9"; shbts="1662219558\\\\054237855618\\\\0541693755558:01f797ac5e7e7ce3a783864a712ce701daf645f0b53ec345daf7c1b10fa260c9dd4426dc"; sessionid=237855618%3AaTfU3dQmbnhBit%3A23%3AAYeXUTjBjMu7aqEViQMWFvAM9RYUldXW89hFYXcl0Q; rur="VLL\\\\054237855618\\\\0541693755575:01f7f9d3e732fb5b95fd7436923c9153e8a46a8d70ac15448a4e229af0d9b0e8872fe46d"\',
                \'dnt\': \'1\',
                \'sec-ch-prefers-color-scheme\': \'dark\',
                \'sec-fetch-dest\': \'document\',
                \'sec-fetch-mode\': \'navigate\',
                \'sec-fetch-site\': \'none\',
                \'sec-fetch-user\': \'?1\',
                \'upgrade-insecure-requests\': \'1\',
                \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',
                \'viewport-width\': \'1229\',
            }

            params = {
                \'__a\': \'1\',
                \'__d\': \'dis\',
            }
            try:
                response = requests.get(f\'https://www.instagram.com/{self.username}/\', params=params, cookies=cookies, headers=headers).json()[\'graphql\'][\'user\'][\'username\']
                response2 = requests.get(f\'https://www.instagram.com/{self.username}/\', params=params, cookies=cookies, headers=headers).json()
                if self.username==response:
                    space()
                    madarchod(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] User found !\')
                    madarchod(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Checking the sincrypt name in the username \')
                    sleep(0.5)
               
                    if self.username.startswith(\'sincrypt\'):
                        madarchod(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Sincrypt Found in username \')
                    else:
                        madarchod(\'\xe2\x94\x94\xe2\x94\x80[ X ] Sincrypt not Found in username \')
                    sleep(1.5)
                    try:
                        space()
                        samay_detail_op = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mDo you want to see details [y/n] : "+r)
                        if samay_detail_op==\'n\' or samay_detail_op==\'N\':
                            if self.username in database_list or self.username in database_list2:
                                madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')
                            else:
                                madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')
                        space()
                        _cls_front_()
                        print(Fore.BLUE+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\
\',end="")
                        print(Fore.GREEN+\'|                  Account Details            /\
\',end="")
                        print(Fore.BLUE+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\
\')
                        saved_username = response2[\'graphql\'][\'user\'][\'username\']
                        saved_userno = response2[\'graphql\'][\'user\'][\'id\']
                        saved_status = response2[\'graphql\'][\'user\'][\'is_private\']
                        saved_bio = response2[\'graphql\'][\'user\'][\'biography\']
                        saved_fullname = response2[\'graphql\'][\'user\'][\'full_name\']
                        if saved_fullname==\'\':
                            saved_fullname = \'No Name\'
                        if saved_bio==\'\':
                            saved_bio = \'No Content\'
                        saved_status = str(saved_status)
                        if saved_status==\'True\':
                            nicesave = \'Private Account\'
                        else:
                            nicesave = \'Public Account\'
                        saved_followers = response2[\'graphql\'][\'user\'][\'edge_followed_by\'][\'count\']
                        saved_follow = response2[\'graphql\'][\'user\'][\'edge_follow\'][\'count\']
                        bussiness_acc = response2[\'graphql\'][\'user\'][\'is_business_account\']
                        prowala = response2[\'graphql\'][\'user\'][\'is_professional_account\']
                        vswale = response2[\'graphql\'][\'user\'][\'business_email\']
                        if vswale==\'None\':
                            savewale = "User Doesn\'t have Business Email"
                        else:
                            savewale = response2[\'graphql\'][\'user\'][\'business_email\']
                        les_wale = response2[\'graphql\'][\'user\'][\'is_joined_recently\']
                        ipswale = response2[\'graphql\'][\'user\'][\'business_phone_number\']
                        popswale = response2[\'graphql\'][\'user\'][\'is_verified\']
                        space()
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Username       :\'+Fore.YELLOW+f\' {saved_username} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Id no          :\'+Fore.YELLOW+f\' {saved_userno} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Account Status :\'+Fore.YELLOW+f\' {nicesave} \
\')
                        print(Fore.MAGENTA+\'||\'+Fore.MAGENTA+\'            Account Bio          ||\
\')
                        space()
                        print(Fore.LIGHTBLUE_EX+f\'{saved_bio.strip()}\
\\t\')
                        space()
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Full Name :\'+Fore.YELLOW+f\' {saved_fullname}\
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Followers :\'+Fore.YELLOW+f\' {saved_followers} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Follow :\'+Fore.YELLOW+f\' {saved_follow} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Bussiness Account :\'+Fore.YELLOW+f\' {bussiness_acc} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Professional Account :\'+Fore.YELLOW+f\' {prowala} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Account Joined Recently :\'+Fore.YELLOW+f\' {les_wale} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Business Email :\'+Fore.YELLOW+f\' {savewale} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Business Number :\'+Fore.YELLOW+f\' {ipswale} \
\',end="")
                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Verified Account :\'+Fore.YELLOW+f\' {popswale} \
\')
                        space()
                        if self.username==\'sincryptayush\':
                            space()
                            madarchod(\'Co-Founder of Team Sincryption\')
                            space()
                            sys.exit()
                        if self.username==\'sincrypt_ace\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            sys.exit()
                        if self.username in database_list and self.username==\'sincryptzork\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'sincryptshark\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'sincrypt_argatics\':
                            space()
                            madarchod(\'Co-Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'sincryptayush\':
                            space()
                            madarchod(\'Co-Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'vaimpier_ritik\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            exit()
                        
                        if self.username in database_list or self.username in database_list2:
                            if self.username==\'sincryptayush\':
                                space()
                                madarchod(\'Co-Founder of Team Sincryption\')
                                space()
                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')
                        else:
                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')
                        space()

                    #
                    except:
                        if self.username==\'sincrypt_ace\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            sys.exit()
                        if self.username==\'sincryptayush\':
                            space()
                            madarchod(\'Co-Founder of Team Sincryption\')
                            space()
                        if self.username in database_list and self.username==\'sincryptzork\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'sincryptshark\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'sincrypt_argatics\':
                            space()
                            madarchod(\'Co-Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'sincryptayush\':
                            space()
                            madarchod(\'Co-Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list and self.username==\'vaimpier_ritik\':
                            space()
                            madarchod(\'Founder of Team Sincryption\')
                            space()
                            exit()
                        elif self.username in database_list or self.username in database_list2:
                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')
                        else:
                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')
                        space()     
            except:
                if self.username==\'sincrypt_ace\':
                    space()
                    madarchod(\'Founder of Team Sincryption\')
                    space()
                    sys.exit()
                if self.username==\'sincryptayush\':
                        space()
                        madarchod(\'Co-Founder of Team Sincryption\')
                        space()
                if self.username in database_list and self.username==\'sincryptzork\':
                    space()
                    madarchod(\'Founder of Team Sincryption\')
                    space()
                    exit()
                elif self.username in database_list and self.username==\'sincryptshark\':
                    space()
                    madarchod(\'Founder of Team Sincryption\')
                    space()
                    exit()
                elif self.username in database_list and self.username==\'sincrypt_argatics\':
                    space()
                    madarchod(\'Co-Founder of Team Sincryption\')
                    space()
                    exit()
                elif self.username in database_list and self.username==\'sincryptayush\':
                    space()
                    madarchod(\'Co-Founder of Team Sincryption\')
                    space()
                    exit()
                elif self.username in database_list and self.username==\'vaimpier_ritik\':
                    space()
                    madarchod(\'Founder of Team Sincryption\')
                    space()
                    exit()
                elif self.username in database_list or self.username in database_list2:
                    madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')
                else:
                    madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')
                    space()
                    sys.exit()

        elif self.data==2:
            madarchod(\'coming soon ...\')
            sys.exit()

        elif self.data==3:
            os.system(\'python update.py\' if os.name==\'nt\' else \'python3 update.py\')

        else:
            space()
            madarchod(\'Exiting  ..\')
            space()
            sys.exit()




try:
    data_user = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Enter the Desire option : "+r))
except:
    space()
    madarchod(\'Please Choose the option :) \')
    space()
    sys.exit()


if __name__ == \'__main__\':
    Sincrypt = Samay(data_user)
    Sincrypt.functions()
