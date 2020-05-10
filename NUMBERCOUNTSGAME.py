import time
import sys

# GENERAL INSTRUCTION
print("Welcome to Number Count Game!!")
print("Select Yourself, You want to PLAYER 1 OR PLAYER 2")
print("If you want to be PLAYER 1,Enter '1',Else you want to be PLAYER 2,Enter '2'")
n=int(input("Enter:"))

#CHECKING THAT PLAYER OPTION IS EITHER 1 OR 2
if n > 2:
    sys.exit(0)

#INITIALISE TOTALS AS 0
atotal=int(0)
btotal=int(0)

#PREDEFINITION FOR USER SELECTS PLAYER 2 
if n==2:
    btotal=(int(1))
    print "PLAYER 1's turn"
    print "PLAYER 1 selects 1"
    print "PLAYER 1 Total :",btotal

#INITIALIZE FLAG FOR WIN PRDICTION
flag=0

#OPERATION FOR USER SELECTS PLAYER 1
if n==1:
    while True:
        print "PLAYER 1's turn"
        a=int(input('Enter number between 1 to 10:'))
        if a not in range(1,11):
            print "Invalid Number!!"
            time.sleep(10)
            sys.exit(0)
        atotal=atotal+a
        print "PLAYER 1's Total :",atotal
        if atotal>=100:
            flag=1
            break
        print "PLAYER 2's turn"
        b=a-1;
        if (b == 0):
            b=1
        btotal=btotal+b
        print "PLAYER 2 selects ",b
        print "PLAYER 2's Total :",btotal
        if btotal>=100:
            flag=2
            break
    if flag==1:
        print "PLAYER 2 WINS !!"
        time.sleep(15)
    if flag==2:
        print "PLAYER 1 WINS !!" 
        time.sleep(15)

#OPERATION FOR USER SELECTS PLAYER 2
if n==2:
    while True:
        print "PLAYER 2's turn"
        a=int(input('Enter number between 1 to 10:'))
        if a not in range(1,11):
            print("Invalid Number!!")
            time.sleep(10)
            sys.exit(0)
        atotal=atotal+a
        print "PLAYER 2's Total :",atotal
        if atotal>=100:
            flag=1
            break
        print "PLAYER 1's turn"
        b=a-2
        if b<=0:
            b=1
        btotal=btotal+b
        print "PLAYER 1 selects ",b
        print "PLAYER 1's Total:",btotal
        if btotal>=100:
            flag=2
            break
    if flag==2:
        print("PLAYER 2 WINS !!")
        time.sleep(15)
    if flag==1:
        print("PLAYER 1 WINS !!")
        time.sleep(15)

    
