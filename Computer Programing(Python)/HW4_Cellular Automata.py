# Homework 4: 1D cellular automata
# apply runrule 19 times

def run20(p):
 print(p)
 pin = list(p) # copy input list
 pout = runrule(pin) # produce output list
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)


# cell index 0..19
# neibourhood 5
# apply rule to cell index 2..17
def runrule(p):
 pp = 20*[0] # initialise output
 pp[2] = rule1(p,2)
 pp[3] = rule1(p,3)
 pp[4] = rule1(p,4)
 pp[5] = rule1(p,5)
 pp[6] = rule1(p,6)
 pp[7] = rule1(p,7)
 pp[8] = rule1(p,8)
 pp[9] = rule1(p,9)
 pp[10] = rule1(p,10)
 pp[11] = rule1(p,11)
 pp[12] = rule1(p,12)
 pp[13] = rule1(p,13)
 pp[14] = rule1(p,14)
 pp[15] = rule1(p,15)
 pp[16] = rule1(p,16)
 pp[17] = rule1(p,17)

 return pp

def rule1(p,i):
    if p[i-2:i+3:1] == [1,0,1,0,1] or p[i-2:i+3:1] == [0,1,0,0,0]: 
        return 1
    else:  
        return 0

# print a list without space
def prettyprint(p):
 s = "".join([str(e) for e in p])
 print(s)
# get input as string of length 20 characters
# input 10101010101010101010
# output a list of integer 0/1
def getinput():
    p = input().strip()
    p3 = [int(x) for x in p]
    return p3
# p0 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
def main():
    p0 = getinput()
    run20(p0)
     # your own initial pattern and rules, use prettyprint()
    run20mycellular(p0)



def mycellular(p,k):
    if p[k-2:k+3:1] == [1,1,1,1,1] or p[k-2:k+3:1] == [0,1,0,1,0]: 
        return 1
    else:
        return 0

def run20mycellular(p):
 prettyprint(p)
 pin = list(p) # copy input list
 pout = runmycellular(pin) # produce output list
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)
 pin = list(pout)
 pout = runmycellular(pin)
 prettyprint(pout)


def runmycellular(p):
 pp = 20*[0] # initialise output
 pp[2] = mycellular(p,2)
 pp[3] = mycellular(p,3)
 pp[4] = mycellular(p,4)
 pp[5] = mycellular(p,5)
 pp[6] = mycellular(p,6)
 pp[7] = mycellular(p,7)
 pp[8] = mycellular(p,8)
 pp[9] = mycellular(p,9)
 pp[10] = mycellular(p,10)
 pp[11] = mycellular(p,11)
 pp[12] = mycellular(p,12)
 pp[13] = mycellular(p,13)
 pp[14] = mycellular(p,14)
 pp[15] = mycellular(p,15)
 pp[16] = mycellular(p,16)
 pp[17] = mycellular(p,17)
 return pp

main()


