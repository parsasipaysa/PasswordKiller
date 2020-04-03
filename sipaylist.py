from itertools import permutations
from colorama import Fore
import sys
import os
import pyfiglet
from time import sleep

def xs():
    print(Fore.RED+"\n[!]"+Fore.BLUE+" if you dont know, empty enter\n")

def logo():
    print(pyfiglet.figlet_format(" S!PLIST",font = 'epic'))
def print2(arg):
    with open("sipaylist.txt", "a") as f:
        f.write(arg+"\n")    
def answer():
    while True:
        try:
            os.system('clear')
            logo()
            sleep(0.3)
            print(Fore.RED+"\n[HAHA!]"+Fore.YELLOW+" MADE BY PARSA HAMIDI"+"\n")
            sleep(0.3)
            print(Fore.RED+"\n[?]"+Fore.LIGHTBLUE_EX+" How do you information?"+"\n")
            sleep(0.3)
            print(Fore.YELLOW+" \n[1]"+Fore.RED+" I'll answer yor questions\n"+Fore.YELLOW+"\n*************************")
            sleep(0.3)
            print(Fore.YELLOW+" \n[2]"+Fore.RED+" I enter the information myself\n"+Fore.YELLOW+"\n*************************")
            sleep(0.3)
            print(Fore.YELLOW+" \n[3]"+Fore.RED+" Owner Specifications\n"+Fore.YELLOW+"\n*************************")
            sleep(0.3)
            print(Fore.YELLOW+" \n[4]"+Fore.RED+" Exit\n"+Fore.YELLOW+"\n*************************")
            sleep(0.3)
            
            option = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"Select an Option :)"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
            if option == "1":
                os.system('clear')
                lis = ["_", "#", "@"]
                logo()
                xs()
                a = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What is a person's first name? "+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if a == "" or a == None:
                    pass
                else:
                    lis.append(a)
                os.system('clear')
                logo()
                xs()
                b = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What is person's last name?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if b == "" or b == None:
                    pass
                else:
                    lis.append(b)
                os.system('clear')
                logo()
                xs()
                c = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What is name of the person's child?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if c == "" or c == None:
                    pass
                else:
                    lis.append(c)
                os.system('clear')
                logo()
                xs()
                d = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What is person's phone number?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if d == "" or d == None:
                    pass
                else:
                    lis.append(d)
                os.system('clear')
                logo()
                xs()
                e = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What is the name of the person's workplace?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if e == "" or e == None:
                    pass
                else:
                    lis.append(e)
                os.system('clear')
                logo()
                xs()
                f = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"When is person's birthday year?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if f == "" or f == None:
                    pass
                else:
                    lis.append(f)
                os.system('clear')
                logo()
                xs()
                g = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"When is person's birthday month?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if g == "" or g == None:
                    pass
                else:
                    lis.append(g)
                os.system('clear')
                logo()
                xs()
                h = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"When is person's birthday day?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if h == "" or h == None:
                    pass
                else:
                    lis.append(h)
                os.system('clear')
                logo()
                xs()
                br = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What is the name of the person she loves?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if br == "" or br == None:
                    pass
                else:
                    lis.append(br)
                os.system('clear')
                logo()
                xs()
                kr = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"What's his nickname?"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if kr == "" or kr == None:
                    pass
                else:
                    lis.append(kr)
                os.system('clear')
                logo()
                print(Fore.BLUE+"[+]"+Fore.YELLOW+" Pleas wait")
                for i in range(1,len(lis)+1):
                    for permutation in permutations(lis,i):
                        x = (''.join([str(p) for p in permutation]))
                        print2(x)
                input(Fore.BLUE+'[*] '+Fore.GREEN+'OK... The Passwords Were Stored In a File Called ""sipaylist.txt""')
                pr = input(Fore.LIGHTRED_EX+"[?]"+Fore.LIGHTBLUE_EX+" you see sipaylist.txt? y/n  ")
                if pr == "y":
                    fi = open("sipaylist.txt","r")
                    c = fi.read()
                    print(c)
                    input(Fore.RESET+"[*]"+Fore.YELLOW+" ok!"+Fore.GREEN+" :)")
                    os.system('clear')
            elif option == "2":
                os.system('clear')
                logo()
                print(Fore.RED+"\n[!]"+Fore.YELLOW+" MADE BY PARSA HAMIDI"+"\n")
                item = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"PASSWORDLIST"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if item == "":
                    print(Fore.RED+"[!] Pleas Enter"+Fore.mro+":)")
                    sys.exit()
                items = item.split(',')
                items.append("_")
                items.append("#")
                items.append("@")
                print(Fore.BLUE+"[+]"+Fore.YELLOW+" Pleas wait")
                for i in range(1,len(items)+1):
                    for permutation in permutations(items,i):
                        x = (''.join([str(p) for p in permutation]))
                        print2(x)
                input(Fore.BLUE+'[*] '+Fore.GREEN+'OK... The Passwords Were Stored In a File Called ""sipaylist.txt""')
                pr = input(Fore.LIGHTRED_EX+"[?]"+Fore.LIGHTBLUE_EX+" you see sipaylist.txt? y/n  ")
                if pr == "y":
                    fi = open("sipaylist.txt","r")
                    c = fi.read()
                    print(c)
                    input(Fore.RESET+"[*]"+Fore.YELLOW+" ok!"+Fore.GREEN+" :)")
                    os.system('clear')
                else:
                    os.system('clear')
            elif option == "4":
                print("\n"+Fore.RED+"[!] your exit"+Fore.BLUE+" :)")
                sys.exit()
            elif option == "3":
                os.system('clear')
                logo()
                print("""
                Owner name : Parsa Hamidi

                Email : parsa.hamidi70@gmail.com
                
                Telegram ID : @sipay
                
                """)
                input(Fore.BLUE+'\n[*] '+Fore.YELLOW+'OK... (Press Enter to return to the menu!...)')
        except:
            print("\n"+Fore.RED+"[!] your exit"+Fore.BLUE+" :)")
            sys.exit()

answer()
