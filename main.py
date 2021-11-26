from scrapper import Scrapper
from proxy import Proxy
import time
import json
import speedtest
import threading
import sys
import os
import itertools

print("""
** This is for research purposes only **
██╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ ██████╗ ██╗██╗     ██╗     ██╗ █████╗ ███╗   ██╗████████╗██╗  ██╗
╚██╗ ██╔╝██║   ██║██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██║██║     ██║     ██║██╔══██╗████╗  ██║╚══██╔══╝██║  ██║
 ╚████╔╝ ██║   ██║█████╔╝ █████╗  ██████╔╝██████╔╝██║██║     ██║     ██║███████║██╔██╗ ██║   ██║   ███████║
  ╚██╔╝  ██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗██╔══██╗██║██║     ██║     ██║██╔══██║██║╚██╗██║   ██║   ██╔══██║
   ██║   ╚██████╔╝██║  ██╗███████╗██████╔╝██║  ██║██║███████╗███████╗██║██║  ██║██║ ╚████║   ██║   ██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
-> FOLLOW MY INSTAGRAM @yukebrillianth <-                                                                                                        
""")


def get_final_speed():
    rawspeed = speedtest.Speedtest().download()
    roundedspeed = round(rawspeed)
    finalspeed = roundedspeed / 1e+6
    return finalspeed


done = False


def animate(txt):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            c = 'OK\n'
        lt = '\r' + txt + ' ' + c
        sys.stdout.write(lt)
        sys.stdout.flush()
        time.sleep(0.1)
        if done and (c == 'OK\n'):
            break


threading.Thread(target=animate, args=(
    "Sedang memeriksa kecepatan internet anda..",)).start()

speedInternet = get_final_speed()
done = True

time.sleep(1)
print("Kecepatan internet anda : %s Mbps" % (speedInternet))
print("Bot dimulai..")

if(speedInternet <= 2):
    threading.Thread(target=animate, args=(
        "Internet anda kurang mendukung atau dibawah 2 mbps..",)).start()
    time.sleep(2)
    done = True
    sys.exit(0)
    os._exit(0)


def loadConfig():
    with open("./config.json") as file:
        return json.load(file)


Proxy = Proxy()
KEYWORD = loadConfig()["keyword"]
WEBSITE_URI = loadConfig()["website_uri"]

if loadConfig()["use_proxy"]:
    AMOUNT = Proxy.importProxy()
else:
    AMOUNT = loadConfig()["amount"]

if loadConfig()["interval"] != "Default":
    INTERVAL = loadConfig()["interval"]
else:
    INTERVAL = 4200

for i in range(0, AMOUNT):
    Scrapper = Scrapper()
    Scrapper.searchGoogleByKeyword(KEYWORD, WEBSITE_URI)
    time.sleep(INTERVAL)
