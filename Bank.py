def inac():
    ac1 = int(input("Enter your account number : "))
    ac2 = int(input("Conform your account number : "))
    if ac1 == ac2:
        return (ac1)
    else :
        print("Account Number did not matched!\nTry Again!!")
def bod(mn):
    l = True
    d = {}
    ac = inac()
    bal = mn
    d[ac] = bal
    while l == True:
        c = int(input("ENTER 1 FOR DEPOSIT\nENTER 2 FOR WITHDRAW\nENTER 3 FOR DISPLAY ACCOUNT INFORMATION\n"))
        if c == 1:
            depo = float(input("Enter amount to deposit : "))
            if depo > 0:
                bal += depo
                d[ac] = bal
                print("Transaction done successfully!\nBalance : ",bal)
            else:
                 print("Value given in negative")
        elif c == 2:
            wit = float(input("Enter amount to withdraw : "))
            if (bal - wit)>mn and wit>0: 
                bal -= wit
                d[ac] = bal
                print("Transaction done successfully!\nBalance : ",bal)
            elif wit<0:
                print("Value given in negative!")
            else:
                print("Minimun balance requirement did not meet!")
        elif c == 3:
            print("ACCOUNT NUMBER\t\tBALANCE")
            print(ac,"\t\t",d[ac])
        else:
            print("Don't play with the system!!")
    l = int(input("Enter '1' for trying again : "))
    
print("WELCOME TO THE OPTIMUS PRIME SUPER BANKING SERVICE!")

loop = True
while loop == True:
    a = int(input("ENTER 1 FOR CURRENT\nENTER 2 FOR SAVINGS BANK\n"))
    if a == 1:
        mn = 1000
        bod(mn)
    elif a == 2:
        m = 500
        bod(m)
    else:
         print("Don't play with the system!!")
    loop = int(input("Enter '1' for trying again : "))
