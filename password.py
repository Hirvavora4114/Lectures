fname=input("First Name")
mname=input("Middle Name")
lname=input("Last Name")
full_name=" ".join([fname, mname ,lname])
print(full_name)
email=input("Enter email id: ")
list1=["com", "org", "edu", "in"]
for word in list1:
    if email.endswith(word):
     print("Valid Email")
    else:
        print("Invalid")
fname=fname.lower()
a=fname [0:4]
dob=input("DDMMYYYY")
b=dob [0:4]
password=a+b
print(password)