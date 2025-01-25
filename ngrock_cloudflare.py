from main import check_intr, error, nrml, red, green, info, root, nc, bcyan, ask, success, info2, yellow
from server import killer, get_credentials
from os import system, popen
import os
from time import sleep

# Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False


def cld_ngr_install():
    check_intr()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
    if True:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
                    print("\n"+info+"Installing "+pkgs[pkg].upper()+nc+nrml)
                    system("sudo pacman -S "+pkgs[pkg]+" --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            print("\n"+error+"Unsupported package manager. Install packages manually!"+nc+nrml)
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        print(error+"PHP cannot be installed. Install it manually!"+nrml)
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        print(error+"Unzip cannot be installed. Install it manually!"+nrml)
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        print(error+"Curl cannot be installed. Install it manually!"+nrml)
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not os.path.isfile(root+"/.ngrokfolder/ngrok"):
        print("\n"+info+"Downloading ngrok....."+nc+nrml)
        check_intr()
        system("rm -rf ngrok.zip ngrok.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.tgz -O ngrok.tgz")
                system("tar -zxf ngrok.tgz > /dev/null 2>&1 && rm -rf ngrok.tgz")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1 ")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
            else:
                system("wget -q --show-progress https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
                system("unzip ngrok.zip > /dev/null 2>&1")
            elif x.find("arm64")!=-1:
                system("wget -q --show-progress 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!"+nrml)
                sleep(3)
        else:
            print(f"{error}Device not supported!"+nrml)
            exit(1)
        system("rm -rf ngrok.zip && mkdir $HOME/.ngrokfolder")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not os.path.isfile(root+"/.cloudflaredfolder/cloudflared"):
        print("\n"+info+"Downloading cloudflared....."+nc+nrml)
        check_intr()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!"+nrml)
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!"+nrml)
                sleep(3)
        else:
            print(f"{error}Device not supported!"+nrml)
            exit(1)
        system("mkdir $HOME/.cloudflaredfolder")
        system("mv -f cloudflared $HOME/.cloudflaredfolder")
        if sudo:
            system("sudo chmod +x $HOME/.cloudflaredfolder/cloudflared")
        else:
            system("chmod +x $HOME/.cloudflaredfolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        print(error+"Previous php still running! Please restart terminal and try again"+nc+nrml)
        exit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        print(error+"Previous ngrok still running. Please restart terminal and try again"+nc+nrml)
        exit()
    else:
        system("chmod +x $HOME/.cloudflaredfolder/cloudflared")

# INSTALL PACKAGES
pkgs=[ "php", "curl", "wget", "unzip"]

# FOR TERMUX & MAC
def installer(package_manager):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            print("\n"+info+"Installing "+pkgs[pkg].upper()+nc+nrml)
            system(package_manager+" install -y "+pkgs[pkg])

def custom_url_ask(url):
    cust= input("\n"+ask+bcyan+"Want to try custom link?(y or press enter to skip) > "+nrml)
    if not cust=="":
        masking(url)
    get_credentials()

# FOR LINUX
def sudoinstaller(package_manager):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            print(info+"Installing "+pkgs[pkg].upper()+nc+nrml)
            system("sudo "+package_manager+" install -y "+pkgs[pkg])

def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    check_intr()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        print(error+"Service not available")
        get_credentials()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter custom domain(Example: google.com, yahoo.com > ")
    if domain=="":
        print("\n"+error+"No domain!")
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            print("\n"+error+"No bait word!")
            print("\n"+success+"Your url is > https://"+ main)
            get_credentials()
        if bait.find(" ")!=-1:
            print("\n"+error+"Space in bait word!")
            get_credentials()
        final= "https://"+bait+"@"+main
        print("\n"+success+"Your url is > "+ final)
        get_credentials()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Enter bait words without space and hyphen (Example: free-money, pubg-mod) > ")
        if (bait==""):
            print("\n"+error+"No bait word!")
            final= domain+"@"+main
            print("\n"+success+"Your url is > "+ final)
            get_credentials()
        if bait.find(" ")!=-1:
            print("\n"+error+"Space in bait word!")
            get_credentials()
        final= domain+"-"+bait+"@"+main
        print("\n"+success+"Your url is > "+ final)
        get_credentials()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Enter bait words without space and hyphen(Example: free-money, insta followers) > ")
        if bait=="":
            print("\n"+error+"No bait word!")
            final= domain+"@"+main
            print("\n"+success+"Your url is > "+ final)
            get_credentials()
        if bait.find(" ")!=-1:
            print("\n"+error+"Space in bait word!")
            get_credentials()
        final= domain+"-"+bait+"@"+main
        print("\n"+success+"Your url is > "+ final)
        get_credentials()

# FINAL URL'S
def url_manager(url,num1,num2):
    check_intr()
    print("\n"+success+"Your urls are given below: \n")
    system("rm -rf $HOME/.site/ip.txt")
    print(info2+"URL "+num1+" > "+yellow+url)
    if os.path.isfile(root+"/.site/.info.txt"):
        with open(root+"/.site/.info.txt", "r") as inform:
            masked=inform.read()
            print(info2+"URL "+num2+" > "+yellow+masked.strip()+"@"+url.replace("https://",""))
