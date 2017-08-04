# Name    : Hashing
# Version : 1.0.0
# Auther  : Ayman Mahmoud Alaiwah
# facebook: https://www.fb.com/ProgAymanAlaiwah
# github  : https://www.github.com/progaymanalaiwah


import sys,hashlib,re
import ctypes as c 

# Edit Api Interpreter
_get_dict = c.pythonapi._PyObject_GetDictPtr
_get_dict.restype = c.POINTER(c.py_object)
_get_dict.argtypes = [c.py_object]
def get_dict(object):return _get_dict(object).contents.value
 
# Function Main 
def set_code_color(self,code_color) :return  "\x1b[1;{0};40m{1}\x1b[0m".format(code_color,self)

# Function Edit Text Colors
def red(self)     :return set_code_color(self,31) 
def green(self)   :return set_code_color(self,32) 
def yellow(self)  :return set_code_color(self,33) 
def blue(self)    :return set_code_color(self,34) 


# Add Function Text Colors To Class String The Private Python Using 
# Library ctypes API The Edit is On Interpreter Python
get_dict(str)['red']     = red
get_dict(str)['green']   = green
get_dict(str)['yellow']  = yellow
get_dict(str)['blue']    = blue



class BruteforceAttackHash:
    def __init__(self,):
        pass

    # Function Create Words Because Encreption To Hash
    def createWords(self,Range,typeAlpha,encryHash,typeHash):
        alpha  = ''
        RangeStart,RangeEnd = re.split(r'[_-]',Range)
        self.typeHash = typeHash
        self.encyHash = encryHash #'86318e52f5ed4801abe1d13d509443de'
        if RangeStart == "0":
            self.Help()
            return False
        if typeAlpha == 'all':
            alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"\$?Ж%& /()=?-.:\\*'-_:.;,"
        else:
            if typeAlpha.find('a') != -1: alpha += "abcdefghijklmnopqrstuvwxyz"
            if typeAlpha.find('A') != -1: alpha += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if typeAlpha.find('d') != -1: alpha += "1234567890"
            if typeAlpha.find('s') != -1: alpha += "! \"\$?Ж%&/()=?-.:\\*'-_:.;,+#"

        def crack (shift):
            rawString = []
            for pushRawString in range(shift):
                rawString.append(0)
            while True:
                for i in range(shift):
                    if rawString[i] > len(alpha) - 1:
                        if i == shift-1 :
                            return False
                        rawString[i+1]+=1
                        rawString[i]=0
                word = ""                     
                for i in range(shift):
                    word+=alpha[rawString[i]]
                if self.checkHash(word) == True:
                    print(' -----------------------------------------------')
                    print(" This One : ".green()+self.encyHash.blue() +" [ "+ "{0}".format(word).green() +" ]")      
                    return "ok"
                rawString[0]+=1
                
                if rawString[shift-1]>len(alpha):break
        for shift in range(int(RangeStart),int(RangeEnd)+1):
            ok = crack(shift)
            if ok == "ok":break

    def encryptionWord(self,typeHash,Word):
        Hash = hashlib.new(typeHash)
        Hash.update(Word.encode())
        Hash = Hash.hexdigest()
        return Hash

    def checkHash(self,Word):
        self.encyWord = self.encryptionWord(self.typeHash,Word)
        self.encyHash = self.encyHash
        if self.encyWord == self.encyHash:return True
        print(" Not This : ".red()+self.encyWord.blue() + " [ "+ "{0}".format(Word).red() +" ]")
        if self.encyWord != self.encyHash: return False
    def Help(self):
        print("""
    ---------------------------------
    A = [ ABCDEFGHIJKLMNOPQRSTUVWXYZ ]
    a = [ abcdefghijklmnopqrstuvwxyz ]
    d = [ 0123456789 ]
    s = [ !\"\$?Ж%&/()=?-.:\\*'-_:.;,]
    alpah all lower and upper and number and symbol
                                                    
    Example : Decrypt2 daAs  1-5   md5        286d5e78aebba5f8f91f4da4984f65fb
    Example : Decrypt2 das  5-10  dsaWithSHA  69d04c58731187c39b44d60cd8acccf02dd392b3
    Example : Decrypt2 aAs  1-15  mdc2        17354123e7f22b27e9a04b1fdcbc38a5
    
    Alpha     = daAs or all
    Range     = 1-5
    typeHash  = md5
    Hahs      = 286d5e78aebba5f8f91f4da4984f65fb
    ----------------[ Type Hash ]---------------
    ['SHA256', 'SHA512', 'dsaWithSHA', 'mdc2', 
    'SHA224', 'MD4', 'sha256', 'sha512', 'ripemd160',
        'whirlpool', 'SHA1', 'MDC2', 'SHA', 'SHA384', 'ecdsa-with-SHA1', 
        'md4', 'md5', 'sha1', 'DSA-SHA', 'sha224', 'dsaEncryption', 'DSA', 'RIPEMD160', 
        'sha', 'MD5', 'sha384']
        """.yellow())


BruteforceAttackHash = BruteforceAttackHash()
try:
    # @var Alpah 
    # a == Latter Lower A == Latter Upper d == Number s == (=)\/*$%^&!
    alpha     = sys.argv[1]
    # @var Range
    # Rnage Word start To end length 
    Rnage     = sys.argv[2]
    # Typehash
    # hash (md5,sha1,sha224,)
    typeHash  = sys.argv[3]
    # hash Example : 286d5e78aebba5f8f91f4da4984f65fb
    encryHash = sys.argv[4]
    BruteforceAttackHash.createWords(Rnage,alpha,encryHash,typeHash)
except KeyboardInterrupt:
    print('Error Keyboard Interrupt'.red())
except:
    BruteforceAttackHash.Help()
