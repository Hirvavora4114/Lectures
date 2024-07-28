#Code for Phone and Laptop Budget
a=int(input("Enter your choice 1 or 2:"))
if(a==1):
    bug=int(input("Enter your buget for phone:"))
    if(bug>10000 and bug<20000):
        print("Samsung,Xaomi,Motorola,Mi")
    elif(bug>20000 and bug<50000):
        print("Oppo,Vivo,Iphone")
    else:
        print("Not available")
elif(a==2):
    bug=int(input("Enter your buget for laptop:"))
    if(bug>10000 and bug<20000):
        print("Samsung,Jio,HP")
    elif(bug>20000 and bug<50000):
        print("Dell,Apple,Samsung")
    else:
        print("Not available")  
else:
    print("Invalid Choice")

