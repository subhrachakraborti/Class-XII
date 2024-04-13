n = int(input("Enter no. of students = "))
ch = eval(input("Enter marks of Chemistry for each students respectively in a list : "))
ph = eval(input("Enter marks of Physics for each students respectively in a list : "))
mt = eval(input("Enter marks of Mathematics for each students respectively in a list : "))
eg = eval(input("Enter marks of English for each students respectively in a list : "))
cs = eval(input("Enter marks of Computer Science for each students respectively in a list : "))
print("1. Enter 1 to do AVERAGE.")
print("2. Enter 2 to sort a SUBJECT.")
c = int(input("Enter your choice : "))
if c == 1:
    for i in range(n):
        mean = (ch[i] + ph[i] + mt[i] + eg[i] + cs[i])/5
        print("Mean Marks for Student",(i+1),"=",mean)
elif c == 2:
    print("Enter ch for Chemistry")
    print("Enter ph for Physics")
    print("Enter mt for Mathematics")
    print("Enter eg for English")
    print("Enter cs for Computer Science")
    sub = input("Enter your subject : ")
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
    sr = int(input("Enter 1 for Ascending\nEnter 2 for Desending\n"))
    if sr == 1:
        s = sorted(l)
        print("ASCENDING ORDER MARKS :".s)
    elif sr == 2:
        s = sorted(l)
        print("DESENDING ORDER MARKS :",s[-1::-1])
else:
    print("SORRY CAN'T YOU SEE?")
    print("You have given something else.")
