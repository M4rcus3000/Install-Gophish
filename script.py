import subprocess
import ipaddress
import os
import sys
DIR = "/root/gophish"


def IpCheck(ip):
    try:
        check = ipaddress.ip_address(ip)
        return True
    except:
        return False

def loop(ip):
    while True:
        if(IpCheck(ip)):
            return ip
        else:
            ip = input("Wrong IP format, try again\n")
            continue



if __name__ == '__main__':

#Check directory
    if(os.path.isdir(DIR)):
        subprocess.call(["rm","-rf", DIR])
        subprocess.call(["mkdir", DIR])
    else:
        subprocess.call(["mkdir", DIR])

    subprocess.call(["clear"])

    network = input("Enter your IP where the admin gophish is going to work\n")
    trueNet = loop(network)
    subprocess.call(["clear"])
    subprocess.call(["wget", "-O", "%s/gophish-v0.11.0-linux-64bit.zip"%DIR, "https://github.com/gophish/gophish/releases/download/v0.11.0/gophish-v0.11.0-linux-64bit.zip"])
    subprocess.call(["apt-get", "update", "-y"])
    subprocess.call(["apt-get", "install", "unar", "-y"])
    subprocess.call(["unar","%s/gophish-v0.11.0-linux-64bit.zip"%DIR, "-o", "%s"%DIR])
    string_sed = '\'s/"listen_url": "127.0.0.1:3333"/"listen_url": "%s:3333"/\''%trueNet 
    print("sed -i %s %s/gophish-v0.11.0-linux-64bit/config.json"%(string_sed, DIR))
    os.system("sed -i %s %s/gophish-v0.11.0-linux-64bit/config.json"%(string_sed, DIR))
    subprocess.call(["chmod", "+x", "%s/gophish-v0.11.0-linux-64bit/./gophish"%DIR])
    subprocess.call(["clear"])
    print("Now you must start gophish, is located in: sudo %s/gophish-v0.11.0-linux-64bit/gophish"%DIR)