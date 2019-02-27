from colorama import *
import sys,hashlib,re
import ctypes 

h = hashlib.algorithms_available
print ("______MODUL HASH________")
print ("========================")
for hs in h :
    print (hs)
print ('******************************')

modul = input(Fore.GREEN + "ENTER MODULE  :>" +"\033[0m" )
hashhe = input(Fore.GREEN + "ENTER HASH  :>" +"\033[0m" )
wlist = input(Fore.GREEN +"ENTER WORDLIST  :>" +"\033[0m" )
wrdlist = open(wlist,'r')
ght = 0
for i in wrdlist.readlines():
    i = i.rstrip("\n")
    ght = ght + 1
    hach = hashlib.new(modul)
    i = i.encode('utf-8')
    hach.update(i) 
    hach.hexdigest()
    if hashhe == hach.hexdigest() :
        print ("\n")
        print (Fore.YELLOW + hach.hexdigest() +"\033[0m " +" PASSWORD :  " + Fore.GREEN + "     "+ str(i) +"\033[0m ")
        
        break
        wrdlist.close()
    else :
        print (Fore.RED + "[*]"+ "\033[0m ",Fore.RED  +"len__"+ "\033[0m " , ght ,Fore.GREEN +"___pass___"+"\033[0m " ,Fore.LIGHTCYAN_EX + str(i) + "\033[0m ")
