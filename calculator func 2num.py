def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
c=int(input('''Enter your choice
             1:add
             2:sub
             3:mul
             4:div'''))
no1=int(input("1st"))
no2=int(input("2nd"))
if c==1:
   sum=add(no1,no2)
   print("Ans:",sum)
elif c==2:
   diff=sub(no1,no2)
   print("Ans:",diff)
elif c==3:
   product=mul(no1,no2)
   print("Ans:", product)
elif c==4:
   quotient=div(no1,no2)
   print("Ans:", quotient)
else:
    print("Invalid choice")