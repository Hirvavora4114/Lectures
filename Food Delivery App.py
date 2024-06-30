#Food Delivery App
Foodchoice=input("Breakfast,Lunch,Dinner")
if(Foodchoice=="Breakfast"):
    cuisine=input("South Indian or Gujarati")
    if(cuisine=="South Indian"):
        food=input("Idli or Dosa")
        if(food=="Idli"):
            print("You have ordered Idli")
        elif(food=="Dosa"):
            print("You have ordered Dosa")
    elif(cuisine=="Gujarati"):
        food=input("Khamand or Jalebi Fafda") 
        if(food=="Khamand"):
            print("You have ordered Khamand")
        elif(food=="Jalebi Fafda"):
            print("You have ordered Jalebi Fafda")
elif(Foodchoice=="Lunch"):
    cuisine=input("North Indian or Thai")
    if(cuisine=="North Indian"):
        food=input("Paratha or Chole Bhature")
        if(food=="Paratha"):
            print("You have ordered Paratha")
        elif(food=="Chole Bhature"):
            print("You have ordered Chole Bhature")
    elif(cuisine=="Thai"):
        food=input("Pad Thai or Thai Curry")
        if(food=="Pad Thai"):
            print("You have ordered Pad Thai")
        elif(food=="Thai Curry"):
            print("You have ordered Thai Curry")
elif(Foodchoice=="Dinner"):
    cuisine=input("Mexican or Italian")
    if(cuisine=="Mexican"):
        food=input("Tacos or Enchiladas")
        if(food=="Tacos"):
            print("You have ordered Tacos")
        elif(food=="Enchiladas"):
            print("You have ordered Enchiladas")
    elif(cuisine=="Italian"):
        food=input("Lasagne or Pizza")
        if(food=="Lasagne"):
            print("You have ordered Lasagne")
        elif(food=="Pizza"):
            print("You have ordered Pizza")
else:
    print("Invalid Foodchoice")
    






    




        


        
