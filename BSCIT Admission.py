def Admission():
 course=input("Enter course name: ")
 if course=="BSCIT":
   per=int(input("Enter your 12th percentage: "))
   sub=input("Enter  subject name: ")
   if sub=='Maths' and per>=50:
          print(" Admission successful! ")
   else:
         print("Admission not successful")
 else:
     print("Enter suitable course")


Admission()