import os, sys, time, socket, argparse, json
from os import popen, system
from time import sleep
from subprocess import run
from server import requirements

version = "TenebrisOS edition"
# ANSI COLOURS
black="\033[0;30m"
red="\033[0;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
wr="\x1b[93;99;95m"

root= popen("cd $HOME && pwd").read().strip()

# SYMBOLS
ask = green + '[' + white + '?' + green + '] '+ blue
success = yellow + '[' + white + '√' + yellow + '] '+green
error = blue + '[' + white + '!' + blue + '] '+red
info= yellow + '[' + white + '+' + yellow + '] '+ cyan
info2= green + '[' + white + '•' + green + '] '+ purple
nrml=white

with open("sites.json", "r") as f:
    json_files=json.load(f)

sites=[]

for site in json_files:
    sites.append(site)

# Website chooser
def options(list):
    print("\n"+ask+"Choose one of the following sites :\n"+nrml)
    i=0
    for site in list:
        i+=1
        print(blue+str(i)+nrml+" "+site)

    choice=list[int(input("\n"+info2+"#user> "+nrml))-1]
    return choice

# socket.setdefaulttimeout(30)
def check_intr(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
    except socket.error:
        print(error+"No internet!")
        time.sleep(2)
        check_intr()


# MAIN FUNCTION
def main():
    while True:
        if os.path.exists(root+"/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    while True:
        choice=options(sites)
        if choice != None or " " or "":
            try:
                with open("sites/"+choice+".json") as phs:
                    json_phis=json.load(phs)
                choicesnbr=[]
                for choice0 in json_phis:
                    choicesnbr.append(choice0)

                choices=[]
                for choice00 in choicesnbr:
                    choices.append(json_phis[choice00])
                choice1=options(choicesnbr)
                requirements(folder=json_phis[choice1])
            except:
                print("\n"+error+"Wrong input!"+nrml)
                main()
        else:
            print("\n"+error+"Wrong input"+nrml)
            main()

if __name__ == '__main__':
    print("Version: ", version)
    print("Main creator: CodingSangh")
    print("Editor: TenebrisOS")
    main()