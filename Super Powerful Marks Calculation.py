n = int(input("Enter no. of students = "))
ph = []
ch = []
mt = []
eg = []
cs = []
s = []
for i in range(n):
    print("\nEnter Details for Student",(i+1))
    ph.append(int(input("Enter Marks in Physics : ")))
    ch.append(int(input("Enter Marks in Chemistry : ")))
    mt.append(int(input("Enter Marks in Mathematics : ")))
    eg.append(int(input("Enter Marks in English : ")))
    cs.append(int(input("Enter Marks in Computer Science : ")))
    print("\n")
print("1. Enter 1 to do AVERAGE.")
print("2. Enter 2 to sort a SUBJECT.")
c = int(input("Enter your choice : "))
if c == 1:
    for i in range(n):
        mean = (ch[i] + ph[i] + mt[i] + eg[i] + cs[i])/5
        print("\nMean Marks for Student",(i+1),"=",mean)
elif c == 2:
    print("Enter ch for Chemistry")
    print("Enter ph for Physics")
    print("Enter mt for Mathematics")
    print("Enter eg for English")
    print("Enter cs for Computer Science")
    sub = input("\nEnter your subject : ")
    if sub == 'ch':
        l = ch
    elif sub == 'ph':
        l = ph
    elif sub == 'mt':
        l = mt
    elif sub == 'eg':
        l = eg
    elif sub == 'cs':
        l = cs
    sr = int(input("\nEnter 1 for Ascending\nEnter 2 for Desending\n"))
    if sr == 1:
        s = sorted(l)
        print("ASCENDING ORDER MARKS :",s)
    elif sr == 2:
        s = sorted(l)
        print("DESENDING ORDER MARKS :",s[-1::-1])
else:
    print("SORRY CAN'T YOU SEE?")
    print("You have given something else.")
