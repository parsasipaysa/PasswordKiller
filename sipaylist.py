from itertools import permutations
from colorama import Fore
import sys
import os
from time import sleep
import pyfiglet

def xs():
    print(Fore.RED+"\n[!]"+Fore.BLUE+" if you dont know, empty enter\n")

def logo():
    print(Fore.RED+pyfiglet.figlet_format("sipay",font = 'epic'))
    print(Fore.YELLOW+pyfiglet.figlet_format("list",font = 'epic'))
def print2(arg):
    with open("sipaylist.txt", "a") as f:
        f.write(arg+"\n")    
def answer():
    while True:
        try:
            os.system('clear')
            logo()
            sleep(0.2)
            print(Fore.RED+"\n[HAHA!]"+Fore.YELLOW+" MADE BY PARSA HAMIDI"+"\n")
            sleep(0.2)
            print(Fore.RED+"\n[?]"+Fore.LIGHTBLUE_EX+" How do you information?"+"\n")
            sleep(0.2)
            print(Fore.YELLOW+" \n[1]"+Fore.RED+" I'll answer yor questions\n"+Fore.YELLOW+"\n*************************")
            sleep(0.2)
            print(Fore.YELLOW+" \n[2]"+Fore.RED+" I enter the information myself\n"+Fore.YELLOW+"\n*************************")
            sleep(0.2)
            print(Fore.YELLOW+" \n[3]"+Fore.RED+" Owner Specifications\n"+Fore.YELLOW+"\n*************************")
            sleep(0.2)
            print(Fore.YELLOW+" \n[4]"+Fore.RED+" Exit\n"+Fore.YELLOW+"\n*************************")
            sleep(0.2)
            
            option = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"Select an Option :)"+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
            if option == "1":
                os.system('clear')
                lis = []
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
                has = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"# "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if has == "y" or has == "Y":
                    lis.append("#")
                else:
                    pass

                star = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"* "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if star == "y" or star == "Y":
                    lis.append("*")
                else:
                    pass

                plus = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"+ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if plus == "y" or plus == "Y":
                    lis.append("+")
                else:
                    pass

                dar = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"% "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if dar == "y" or dar == "Y":
                    lis.append("%")
                else:
                    pass

                boz = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"> "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if boz == "y" or boz == "Y":
                    lis.append(">")
                else:
                    pass

                koc = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"< "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if koc == "y" or koc == "Y":
                    lis.append("<")
                else:
                    pass

                under = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"_ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if under == "y" or under == "Y":
                    lis.append("_")
                else:
                    pass

                do = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+": "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if do == "y" or do == "Y":
                    lis.append(":")
                else:
                    pass

                par1 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"( "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if par1 == "y" or par1 == "Y":
                    lis.append("(")
                else:
                    pass

                par2 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+") "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if par2 == "y" or par2 == "Y":
                    lis.append(")")
                else:
                    pass

                ad = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"@ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if ad == "y" or ad == "Y":
                    lis.append("@")
                else:
                    pass

                dol = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"$ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if dol == "y" or dol == "Y":
                    lis.append("$")
                else:
                    pass

                kur1 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"[ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if kur1 == "y" or kur1 == "Y":
                    lis.append("[")
                else:
                    pass

                kur2 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"] "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if kur2 == "y" or kur2 == "Y":
                    lis.append("]")
                else:
                    pass

                minus = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"- "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if minus == "y" or minus == "Y":
                    lis.append("-")
                else:
                    pass

                sl = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+r"\ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if sl == "y" or sl == "Y":
                    lis.append("\\")
                else:
                    pass

                sl2 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"/ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if sl2 == "y" or sl2 == "Y":
                    lis.append("/")
                else:
                    pass
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
                print(Fore.RED+"\n[!]"+Fore.YELLOW+" press empty enter for go to menu"+"\n")
                item = input(Fore.RED+"  ┌─["+Fore.LIGHTGREEN_EX+"Enter the information and separate with "+Fore.YELLOW+" , "+Fore.BLUE+"~"+Fore.WHITE+"TELEGRAM ID: @SIPAY"+Fore.RED+"/"+Fore.CYAN+"HACK"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"OK..."+Fore.RED+"""]
  └──╼ """+Fore.WHITE+">> ")
                if item == "":
                    answer()
                items = item.split(',')
                has = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"# "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if has == "y" or has == "Y":
                    lis.append("#")
                else:
                    pass

                star = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"* "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if star == "y" or star == "Y":
                    lis.append("*")
                else:
                    pass

                plus = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"+ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if plus == "y" or plus == "Y":
                    lis.append("+")
                else:
                    pass

                dar = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"% "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if dar == "y" or dar == "Y":
                    lis.append("%")
                else:
                    pass

                boz = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"> "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if boz == "y" or boz == "Y":
                    lis.append(">")
                else:
                    pass

                koc = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"< "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if koc == "y" or koc == "Y":
                    lis.append("<")
                else:
                    pass

                under = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"_ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if under == "y" or under == "Y":
                    lis.append("_")
                else:
                    pass

                do = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+": "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if do == "y" or do == "Y":
                    lis.append(":")
                else:
                    pass

                par1 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"( "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if par1 == "y" or par1 == "Y":
                    lis.append("(")
                else:
                    pass

                par2 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+") "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if par2 == "y" or par2 == "Y":
                    lis.append(")")
                else:
                    pass

                ad = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"@ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if ad == "y" or ad == "Y":
                    lis.append("@")
                else:
                    pass

                dol = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"$ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if dol == "y" or dol == "Y":
                    lis.append("$")
                else:
                    pass

                kur1 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"[ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if kur1 == "y" or kur1 == "Y":
                    lis.append("[")
                else:
                    pass

                kur2 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"] "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if kur2 == "y" or kur2 == "Y":
                    lis.append("]")
                else:
                    pass

                minus = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"- "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if minus == "y" or minus == "Y":
                    lis.append("-")
                else:
                    pass

                sl = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+r"\ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if sl == "y" or sl == "Y":
                    lis.append("\\")
                else:
                    pass

                sl2 = input(Fore.LIGHTBLUE_EX+"\nDo you want to be added to the passlist "+Fore.YELLOW+"/ "+Fore.RED+"? "+Fore.GREEN+"y"+Fore.WHITE+"/"+Fore.RED+"n  ")
                if sl2 == "y" or sl2 == "Y":
                    lis.append("/")
                else:
                    pass

                
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
                print("\n"+Fore.RED+"[!] your exit"+Fore.BLUE+" :)\n")
                sys.exit()
            elif option == "3":
                os.system('clear')
                logo()
                print("""
                Owner name : Parsa Hamidi

                Email : parsa.hamidi70@gmail.com
                
                Telegram ID : https://T.me/sipay
                
                """)
                input(Fore.BLUE+'\n[*] '+Fore.YELLOW+'OK... (Press Enter to return to the menu!...)')
        except:
            sys.exit()

answer()
