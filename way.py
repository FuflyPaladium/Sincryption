import zlib
import base64

s = b'==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'
b64 = base64.b64decode(s[::-1])
print(zlib.decompress(b64))

s2 = b'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'
b64 = base64.b64decode(s2[::-1])
print(zlib.decompress(b64))

s3 = b'=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'
b64 = base64.b64decode(s3[::-1])
print(zlib.decompress(b64))

# Original code :
#b'# Team Sincryption\n# Founders : vaimpier , samay , cold , shark \n# Co-Founders : Aayush , Argatics\n# Python programmming \n\n\n# ------imports \nimport os \nimport sys\ntry:\n    import colorama\n    import requests\n    import bs4\nexcept ImportError:\n    os.system(\'pip install colorama\' if os.name==\'nt\' else \'pip install colorama\')\n    os.system(\'pip install requests\' if os.name==\'nt\' else \'pip install requests\')\n    os.system(\'pip install bs4\' if os.name==\'nt\' else \'pip install bs4\')\nfrom colorama import Fore\nfrom time import sleep\nimport requests\nfrom bs4 import BeautifulSoup\n\n\n#------colors \nr = "\\033[1;31m"\ng = "\\033[1;32m"\ny = "\\033[1;33m"\nb = "\\033[1;34m"\nd = "\\033[2;37m"\nR = "\\033[1;41m"\nY = "\\033[1;43m"\nB = "\\033[1;44m"\nw = "\\033[1;37m"\ng = "\\033[0;90m"\ngg = "\\033[1;32m"\ny = r\n\n\n#-----------banner and logos \n\nlogo = \'\'\'\n    \\033[1;31m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97        \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n    \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91        \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n    \\033[0;90m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\\033[1;33m    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\033[1;33m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n    \\033[1;33m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \\033[1;34m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n    \\033[1;35m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91           \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n    \\033[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d           \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d    \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n\'\'\'\n\ndef banner():\n    print(logo)\n\ndef clear():\n    os.system(\'cls\' if os.name==\'nt\' else \'clear\')\n\ndef space():\n    print(\'\\n\')\n\n\ndatabase_list = [\'sincrypt_argatics\',\'sincryptzork\',\'sincryptshark\',\'sincrypt_ace\',\'sincrypt.s3nu\',\'sincryptr4j\',\'sincrypt4drio\',\'sincrypt.s3nu\',\'sincryptx0\',\'sincryptzara\',\'sincryptveer\']\n\ndatabase_list2 = [\n    \'sincryptm4dxt\',\n    \'sincryptg0ku\',\n    \'sincryptayush\',\n    \'sincrypt_n1nja\',\n    \'sincryptrew1sh\',\n    \'sincryptr2dra\',\n    \'sincryptr4drx\',\n    \'sincryptxsl4shu\',\n    \'sincryptrand0m\',\n    \'sincryptdrag0n\',\n    \'sincrypt.vdnt\',\n    \'sincryptl0ve\',\n    \'sincrypts3npa1\',\n    \'sincryptpiyush\',\n    \'sincryptk3n\',\n    \'sincryptsn1p3r\',\n    \'sincrypt.rahul\',\n    \'sincryptxhisoka\',\n    \'sincrypth4wk\',\n    \'sincryptpriyanshu\',\n    \'sincrypteagle\',\n]\n\ndef madarchod(name):\n    print(r+"\xe2\x94\x94\xe2\x94\x80"+w+f"{name}")\n\ndef options():\n    madarchod(\'[ 1 ] Check Username : \')\n    madarchod(\'[ 2 ] About User :\')\n    madarchod(\'[ 3 ] Update :\')\n    madarchod(\'[ 4 ] Exit :\')\n\ndef front_final():\n    clear()\n    banner()\n    space()\n    options()\n    space()\n\ndef _cls_front_():\n    clear()\n    banner()\n    space()\n\nfront_final()\n\nclass Samay:\n    project = \'Sincryption Panel !\'\n    def __init__(self,_user_):\n        self.data = _user_\n    def functions(self):\n        if self.data==1:\n            _cls_front_()\n\n            self.username = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Enter the Instagram Username : "+r)\n            #\n            \n            url = \'https://www.instagram.com\'\n\n            localmids = requests.get(url).cookies[\'mid\']\n            localtoken = requests.get(url).cookies[\'csrftoken\']\n            localigdidi = requests.get(url).cookies[\'ig_did\']\n\n\n            cookies = {\n                \'ig_did\': localigdidi,\n                \'ig_nrcb\': \'1\',\n                \'mid\': localmids,\n                \'datr\': \'BL47YvvCmZh9a49mlTROe_R1\',\n                \'ds_user_id\': \'237855618\',\n                \'csrftoken\': localtoken,\n                \'dpr\': \'1.25\',\n                \'shbid\': \'"12935\\\\054237855618\\\\0541693755558:01f7bd94873a19cc89516f15a2c7cd52f8c1a70666fedb519473d266b6270fba2c0306b9"\',\n                \'shbts\': \'"1662219558\\\\054237855618\\\\0541693755558:01f797ac5e7e7ce3a783864a712ce701daf645f0b53ec345daf7c1b10fa260c9dd4426dc"\',\n                \'sessionid\': \'237855618%3AaTfU3dQmbnhBit%3A23%3AAYeXUTjBjMu7aqEViQMWFvAM9RYUldXW89hFYXcl0Q\',\n                \'rur\': \'"VLL\\\\054237855618\\\\0541693755575:01f7f9d3e732fb5b95fd7436923c9153e8a46a8d70ac15448a4e229af0d9b0e8872fe46d"\',\n            }\n\n            headers = {\n                \'authority\': \'www.instagram.com\',\n                \'accept\': \'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\',\n                \'accept-language\': \'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5\',\n                \'cache-control\': \'max-age=0\',\n                # Requests sorts cookies= alphabetically\n                # \'cookie\': \'ig_did=4552821A-91C2-4A0E-95DD-AAE0D34A7914; ig_nrcb=1; mid=YiTsfQALAAFciQQ2eE0cNnMgdXEK; datr=BL47YvvCmZh9a49mlTROe_R1; ds_user_id=237855618; csrftoken=TLyqyVhTxt9xXK8Q6HD5OqCG41APPHDO; dpr=1.25; shbid="12935\\\\054237855618\\\\0541693755558:01f7bd94873a19cc89516f15a2c7cd52f8c1a70666fedb519473d266b6270fba2c0306b9"; shbts="1662219558\\\\054237855618\\\\0541693755558:01f797ac5e7e7ce3a783864a712ce701daf645f0b53ec345daf7c1b10fa260c9dd4426dc"; sessionid=237855618%3AaTfU3dQmbnhBit%3A23%3AAYeXUTjBjMu7aqEViQMWFvAM9RYUldXW89hFYXcl0Q; rur="VLL\\\\054237855618\\\\0541693755575:01f7f9d3e732fb5b95fd7436923c9153e8a46a8d70ac15448a4e229af0d9b0e8872fe46d"\',\n                \'dnt\': \'1\',\n                \'sec-ch-prefers-color-scheme\': \'dark\',\n                \'sec-fetch-dest\': \'document\',\n                \'sec-fetch-mode\': \'navigate\',\n                \'sec-fetch-site\': \'none\',\n                \'sec-fetch-user\': \'?1\',\n                \'upgrade-insecure-requests\': \'1\',\n                \'user-agent\': \'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1\',\n                \'viewport-width\': \'1229\',\n            }\n\n            params = {\n                \'__a\': \'1\',\n                \'__d\': \'dis\',\n            }\n            try:\n                response = requests.get(f\'https://www.instagram.com/{self.username}/\', params=params, cookies=cookies, headers=headers).json()[\'graphql\'][\'user\'][\'username\']\n                response2 = requests.get(f\'https://www.instagram.com/{self.username}/\', params=params, cookies=cookies, headers=headers).json()\n                if self.username==response:\n                    space()\n                    madarchod(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] User found !\')\n                    madarchod(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Checking the sincrypt name in the username \')\n                    sleep(0.5)\n               \n                    if self.username.startswith(\'sincrypt\'):\n                        madarchod(\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] Sincrypt Found in username \')\n                    else:\n                        madarchod(\'\xe2\x94\x94\xe2\x94\x80[ X ] Sincrypt not Found in username \')\n                    sleep(1.5)\n                    try:\n                        space()\n                        samay_detail_op = input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"\\033[1;37mDo you want to see details [y/n] : "+r)\n                        if samay_detail_op==\'n\' or samay_detail_op==\'N\':\n                            if self.username in database_list or self.username in database_list2:\n                                madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')\n                            else:\n                                madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')\n                        space()\n                        _cls_front_()\n                        print(Fore.BLUE+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\\n\',end="")\n                        print(Fore.GREEN+\'|                  Account Details            /\\n\',end="")\n                        print(Fore.BLUE+\'|\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80/\\n\')\n                        saved_username = response2[\'graphql\'][\'user\'][\'username\']\n                        saved_userno = response2[\'graphql\'][\'user\'][\'id\']\n                        saved_status = response2[\'graphql\'][\'user\'][\'is_private\']\n                        saved_bio = response2[\'graphql\'][\'user\'][\'biography\']\n                        saved_fullname = response2[\'graphql\'][\'user\'][\'full_name\']\n                        if saved_fullname==\'\':\n                            saved_fullname = \'No Name\'\n                        if saved_bio==\'\':\n                            saved_bio = \'No Content\'\n                        saved_status = str(saved_status)\n                        if saved_status==\'True\':\n                            nicesave = \'Private Account\'\n                        else:\n                            nicesave = \'Public Account\'\n                        saved_followers = response2[\'graphql\'][\'user\'][\'edge_followed_by\'][\'count\']\n                        saved_follow = response2[\'graphql\'][\'user\'][\'edge_follow\'][\'count\']\n                        bussiness_acc = response2[\'graphql\'][\'user\'][\'is_business_account\']\n                        prowala = response2[\'graphql\'][\'user\'][\'is_professional_account\']\n                        vswale = response2[\'graphql\'][\'user\'][\'business_email\']\n                        if vswale==\'None\':\n                            savewale = "User Doesn\'t have Business Email"\n                        else:\n                            savewale = response2[\'graphql\'][\'user\'][\'business_email\']\n                        les_wale = response2[\'graphql\'][\'user\'][\'is_joined_recently\']\n                        ipswale = response2[\'graphql\'][\'user\'][\'business_phone_number\']\n                        popswale = response2[\'graphql\'][\'user\'][\'is_verified\']\n                        space()\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Username       :\'+Fore.YELLOW+f\' {saved_username} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Id no          :\'+Fore.YELLOW+f\' {saved_userno} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Account Status :\'+Fore.YELLOW+f\' {nicesave} \\n\')\n                        print(Fore.MAGENTA+\'||\'+Fore.MAGENTA+\'            Account Bio          ||\\n\')\n                        space()\n                        print(Fore.LIGHTBLUE_EX+f\'{saved_bio.strip()}\\n\\t\')\n                        space()\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Full Name :\'+Fore.YELLOW+f\' {saved_fullname}\\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Followers :\'+Fore.YELLOW+f\' {saved_followers} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Follow :\'+Fore.YELLOW+f\' {saved_follow} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Bussiness Account :\'+Fore.YELLOW+f\' {bussiness_acc} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Professional Account :\'+Fore.YELLOW+f\' {prowala} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Account Joined Recently :\'+Fore.YELLOW+f\' {les_wale} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Business Email :\'+Fore.YELLOW+f\' {savewale} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Business Number :\'+Fore.YELLOW+f\' {ipswale} \\n\',end="")\n                        print(Fore.RED+\'>> \'+Fore.GREEN+\'Verified Account :\'+Fore.YELLOW+f\' {popswale} \\n\')\n                        space()\n                        if self.username==\'sincryptayush\':\n                            space()\n                            madarchod(\'Co-Founder of Team Sincryption\')\n                            space()\n                            sys.exit()\n                        if self.username==\'sincrypt_ace\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            sys.exit()\n                        if self.username in database_list and self.username==\'sincryptzork\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'sincryptshark\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'sincrypt_argatics\':\n                            space()\n                            madarchod(\'Co-Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'sincryptayush\':\n                            space()\n                            madarchod(\'Co-Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'vaimpier_ritik\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        \n                        if self.username in database_list or self.username in database_list2:\n                            if self.username==\'sincryptayush\':\n                                space()\n                                madarchod(\'Co-Founder of Team Sincryption\')\n                                space()\n                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')\n                        else:\n                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')\n                        space()\n\n                    #\n                    except:\n                        if self.username==\'sincrypt_ace\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            sys.exit()\n                        if self.username==\'sincryptayush\':\n                            space()\n                            madarchod(\'Co-Founder of Team Sincryption\')\n                            space()\n                        if self.username in database_list and self.username==\'sincryptzork\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'sincryptshark\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'sincrypt_argatics\':\n                            space()\n                            madarchod(\'Co-Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'sincryptayush\':\n                            space()\n                            madarchod(\'Co-Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list and self.username==\'vaimpier_ritik\':\n                            space()\n                            madarchod(\'Founder of Team Sincryption\')\n                            space()\n                            exit()\n                        elif self.username in database_list or self.username in database_list2:\n                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')\n                        else:\n                            madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')\n                        space()     \n            except:\n                if self.username==\'sincrypt_ace\':\n                    space()\n                    madarchod(\'Founder of Team Sincryption\')\n                    space()\n                    sys.exit()\n                if self.username==\'sincryptayush\':\n                        space()\n                        madarchod(\'Co-Founder of Team Sincryption\')\n                        space()\n                if self.username in database_list and self.username==\'sincryptzork\':\n                    space()\n                    madarchod(\'Founder of Team Sincryption\')\n                    space()\n                    exit()\n                elif self.username in database_list and self.username==\'sincryptshark\':\n                    space()\n                    madarchod(\'Founder of Team Sincryption\')\n                    space()\n                    exit()\n                elif self.username in database_list and self.username==\'sincrypt_argatics\':\n                    space()\n                    madarchod(\'Co-Founder of Team Sincryption\')\n                    space()\n                    exit()\n                elif self.username in database_list and self.username==\'sincryptayush\':\n                    space()\n                    madarchod(\'Co-Founder of Team Sincryption\')\n                    space()\n                    exit()\n                elif self.username in database_list and self.username==\'vaimpier_ritik\':\n                    space()\n                    madarchod(\'Founder of Team Sincryption\')\n                    space()\n                    exit()\n                elif self.username in database_list or self.username in database_list2:\n                    madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ \xe2\x9c\x94 ] @{self.username} is verified user of Team Sincryption\')\n                else:\n                    madarchod(f\'\xe2\x94\x94\xe2\x94\x80[ X ] @{self.username} is not verified user of Team Sincryption or may be kicked \')\n                    space()\n                    sys.exit()\n\n        elif self.data==2:\n            madarchod(\'coming soon ...\')\n            sys.exit()\n\n        elif self.data==3:\n            os.system(\'python update.py\' if os.name==\'nt\' else \'python3 update.py\')\n\n        else:\n            space()\n            madarchod(\'Exiting  ..\')\n            space()\n            sys.exit()\n\n\n\n\ntry:\n    data_user = int(input(r+"\xe2\x94\x94\xe2\x94\x80"+w+"Enter the Desire option : "+r))\nexcept:\n    space()\n    madarchod(\'Please Choose the option :) \')\n    space()\n    sys.exit()\n\n\nif __name__ == \'__main__\':\n    Sincrypt = Samay(data_user)\n    Sincrypt.functions()\n\n\n\n\n\n\n'
