from colorama import *
import sys,hashlib,re
import ctypes 
h = hashlib.algorithms_available
print ("______MODUL HASH________")
print ("========================")
for i in h :
    print (i)
print ("==========================")

z = input( Fore.CYAN +"ENTER text :>>" + "\033[0m ")

ent = input(Fore.CYAN + " MODULE hashes :>>" + "\033[0m ")

#print(Fore.GREEN + z + "\033[0m \n"+Fore.GREEN +ent ),"\033[0m \n"
hash_h = hashlib.new(ent)
z = z.encode("utf-8")

hash_h.update(z) 

print (Fore.GREEN + str(z) +"\033[0m " +" is hash :  " + Fore.YELLOW + hash_h.hexdigest()+"\033[0m")
