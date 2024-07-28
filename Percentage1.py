a=int(input("s1: "))
b=int(input("s2: "))
c=int(input("s3: "))
d=int(input("s4: "))
e=int(input("s5: "))
percentage=(a+b+c+d+e)/5
print("percentage",percentage)
if(percentage<35):
  print("fail")
elif(percentage>=35) & (percentage<40):
  print("pass")
elif(percentage>=40) & (percentage<60):
   print("second class")
elif(percentage>=60) & (percentage<75):
   print("first class")
else:
   print("Distinction")