# ============= fragment of code for Homework 3  Encryption ===========

# update 1, 25 aug 2021, 16:45pm

# encryption  inspired by AES (Advanced Encryption Standard)
# Prabhas Chongstitvatana

key = "ABCDEFGHIJKLMNOP"
plaintext = "I LOVE PYTHON101"

def encrypt(key,text):
    t1 = oneround(key,text)
    t2 = oneround(key,t1)
    return t2

def oneround(key,text):
    t1 = addkey(key,text)
    t2 = subbyte(t1)
    t3 = shiftrow(t2)
    t4 = mixcolumn(t3)
    return t4

# xor key with text, keep it in printable range
def addkey(k,t):
    s = doxor(k[0],t[0])
    s += doxor(k[1],t[1])
    s += doxor(k[2],t[2])
    s += doxor(k[3],t[3])
    s += doxor(k[4],t[4])
    s += doxor(k[5],t[5])
    s += doxor(k[6],t[6])
    s += doxor(k[7],t[7])
    s += doxor(k[8],t[8])
    s += doxor(k[9],t[9])
    s += doxor(k[10],t[10])
    s += doxor(k[11],t[11])
    s += doxor(k[12],t[12])
    s += doxor(k[13],t[13])
    s += doxor(k[14],t[14])
    s += doxor(k[15],t[15])
     
    
    return s

# doxor  xor ascii code of two characters c1, c2
#  find ascii value v1 = ord(c1), v2 = ord(c2) then
#  exclusive or (xor) them  v3 = v1 ^ v2
def doxor(c1,c2):
    
    a1 = ord(c1)
    a2 = ord(c2)
    a3 = a1 ^ a2
    
    
    c4 = makeprintable(a3)
    return c4   

def makeprintable(c):
    c1 = ((c % 90) + 32 % 90)
    return chr(c1)

# substitute characters in t with pattern in subinput and suboutput
def subbyte(t):
    s = findreplace(t[0])
    s += findreplace(t[1])
    s += findreplace(t[2])
    s += findreplace(t[3])
    s += findreplace(t[4])
    s += findreplace(t[5])
    s += findreplace(t[6])
    s += findreplace(t[7])
    s += findreplace(t[8])
    s += findreplace(t[9])
    s += findreplace(t[10])
    s += findreplace(t[11])
    s += findreplace(t[12])
    s += findreplace(t[13])
    s += findreplace(t[14])
    s += findreplace(t[15])
    
    return s

# findreplace use subinput and suboutput 
def findreplace(c):  
    i = subinput.find(c)
    c2 = suboutput[i]
    return c2

# these two functions use "for", which we will learn later
# just use it now
def createsubinput():
    s = ""
    for i in range(32,91):
        s += chr(i)
    return s

def createsuboutput():
    s = ""
    for i in range(33,91):
        s += chr(i)
    s += chr(32)
    return s

subinput = createsubinput()
suboutput = createsuboutput()

# rotate string one character to the right
def shiftonce(t):
    t1=t[15]+t[0:15]
    return t1

def shiftrow(t):
    t1 = shiftonce(t)
    t2 = shiftonce(t1)
    return t2

# coefficients use in multiply with fix polynomial in mixcolumn
# fixpoly = "2311123111233112"
# we just hardcode it into the function
def mixcolumn(t):
    s = mulc(t[0], "2")
    s += mulc(t[1], "3")
    s += mulc(t[2], "1")
    s += mulc(t[3], "1")
    s += mulc(t[4], "1")
    s += mulc(t[5], "2")
    s += mulc(t[6], "3")
    s += mulc(t[7], "1")
    s += mulc(t[8], "1")
    s += mulc(t[9], "1")
    s += mulc(t[10], "2")
    s += mulc(t[11], "3")
    s += mulc(t[12], "3")
    s += mulc(t[13], "1")
    s += mulc(t[14], "1")
    s += mulc(t[15], "2")
    
    return s

def mulc(c1,c2):
    c3 = ord(c1) * ord(c2)
    c4 = makeprintable(c3)
    return c4

def test():
    s = ""
    s += "1"
    s += "2"
    print(s)
    txt = "WHATEVER01234567"
    txt2 = subbyte(txt)
    print(txt2)
    txt4 = oneround(key,plaintext)
    print(txt4)
    txt5 = encrypt(key,plaintext)
    print(txt5)
    
def main():
    key  = input('key: ')
    plaintext = input('text: ')
    ciphertext = encrypt(key, plaintext)
    print(ciphertext)

main()

####  End  ######