import random
import requests
import time as mm
import sys as n
from colorama import *
import string

req = requests.session()


def wacn(s):
    for c in s + "\n":
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(0.7 / 150)



def vpn():
    user = ""
    for i in range(15):
        user += random.choice(string.ascii_lowercase)
    urlvpn = f"https://instagram.com/{user}"
    headersvpn = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    sendvpn = req.get(urlvpn, headers=headersvpn)
    if sendvpn.status_code == 404:
        wacn(f"{Fore.LIGHTGREEN_EX}Your not blocked")
    else:
        wacn(f"{Fore.LIGHTRED_EX}Your blocked use a VPN")
    exit()


def checksessionid():
    sessionid = input(f"{Fore.LIGHTWHITE_EX}Enter session Id: ")
    user = ""
    for i in range(8):
        user += random.choice(string.ascii_lowercase)
    urlchecksession = f"https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id={user}&app_language=ar"
    datachecksession = ""
    headerschecksession = {
        "Accept": "text/html,application/xhtml+xml,applicationxml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    cookieschecksession = {'sessionid': sessionid}
    sendchecksession = req.get(urlchecksession, data=datachecksession, headers=headerschecksession, cookies=cookieschecksession)
    jsonsendchecksession = str(sendchecksession.json()["status_msg"])
    if jsonsendchecksession == "" or "":
        wacn(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}The session isnt blocked")
    else:
        wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}The session is blocked")
    exit()


def checkersession(sessionid, user, count):
    urlcheckersession = f"https://www.tiktok.com/api/uniqueid/check/?region=US&aid=1233&unique_id={user}&app_language=ar"
    datacheckersession = ""
    headerscheckersession = {
        "Accept": "text/html,application/xhtml+xml,applicationxml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    cookiescheckersession = {'sessionid': sessionid}
    sendchecksession = req.get(urlcheckersession, data=datacheckersession, headers=headerscheckersession, cookies=cookiescheckersession)
    jsonsendcheckersession = str(sendchecksession.json()["status_msg"])
    if jsonsendcheckersession == "" or "":
        print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTGREEN_EX}تم الصيد")
        with open("found.txt", "a") as found:
            found.write(user + "\n")
    else:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTRED_EX}لم يتم الصيد")


def checkerwithoutsession(user, count):
    urlcheckerwithoutsession = f"https://www.tiktok.com/@{user}?"
    headerscheckerwithoutsession = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "www.tiktok.com",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0"
    }
    sendcheckerwithoutsession = req.get(urlcheckerwithoutsession, headers=headerscheckerwithoutsession)
    if sendcheckerwithoutsession.status_code == 404:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTGREEN_EX} Available but it may be banned")
        with open("found.txt", "a") as found:
            found.write(user + "\n")
    else:
        print(f"{Style.BRIGHT}{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}{count}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}{user}: {Fore.LIGHTRED_EX} Unavailable")


wacn(f"""{Style.BRIGHT}{Fore.LIGHTYELLOW_EX} TikTok Ahmdoquit
Use this tool and have fun!
░█████╗░██╗░░██╗███╗░░░███╗██████╗░░█████╗░
██╔══██╗██║░░██║████╗░████║██╔══██╗██╔══██╗
███████║███████║██╔████╔██║██║░░██║██║░░██║
██╔══██║██╔══██║██║╚██╔╝██║██║░░██║██║░░██║
██║░░██║██║░░██║██║░╚═╝░██║██████╔╝╚█████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═════╝░░╚════╝░
                                                        
{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================
        {Style.BRIGHT}{Fore.LIGHTWHITE_EX}[1] User checker
        {Style.BRIGHT}{Fore.LIGHTCYAN_EX}   
       (TikTok Ahmdoquit on top)
{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================""")
choose = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Pick a number: ")
wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
if choose == "4":
    vpn()
elif choose == "2":
    checksessionid()
elif choose == "3":
    wacn(f"""{Style.BRIGHT}{Fore.LIGHTWHITE_EX}
        [1] Pick from file
        [2] Random Choosing""")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    lastchoice = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Pick a Number: ")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    if lastchoice == "1":
        sesssionid = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Enter the session ID: ")
        fileinput = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Choose from files: ").strip()
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        users = open(fileinput, "r").read().splitlines()
        count = 0
        for user in users:
            if user == "":
                wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Thanks For using my tool")
                exit()
            else:
                count += 1
                checkersession(sesssionid, user, count)
    elif lastchoice == "2":
        sesssionid = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}enter session id: ")
        amount = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}how many users: "))
        length = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}length of users: "))
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        count = 0
        chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for _ in range(amount):
            user = ""
            for _ in range(length):
                user += random.choice(chars)
            count += 1
            checkersession(sesssionid, user, count)
        wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}thanks for using my tool.")
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        exit()
    else:
        wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}fool you will find nothing.")
elif choose == "1":
    wacn(f"""{Style.BRIGHT}{Fore.LIGHTWHITE_EX}
            [1] Check by entering 1""")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    lastchoice = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Pick a number ")
    wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
    if lastchoice == "02831":
        fileinput = input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}اختيار من الملفات: ").strip()
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        users = open(fileinput, "r").read().splitlines()
        count = 0
        for user in users:
            if user == "":
                wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Thanks for using my tool")
                exit()
            else:
                count += 1
                checkerwithoutsession(user, count)
    elif lastchoice == "1":
        amount = 900000000
        length = int(input(f"{Style.BRIGHT}{Fore.LIGHTWHITE_EX}Letters of the user? "))
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        count = 0
        chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
        for _ in range(amount):
            user = ""
            for _ in range(length):
                user += random.choice(chars)
            count += 1
            checkerwithoutsession( user, count)
        wacn(f"{Style.BRIGHT}{Fore.LIGHTBLUE_EX}Thanks for using my tool")
        wacn(f"{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}===========================================================")
        exit()
    else:
        wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Restart the program you have made an error!")
else:
    wacn(f"{Style.BRIGHT}{Fore.LIGHTRED_EX}Restart the program you have made an error!")
