#=======================================================================
#    Project    9:    Decision Maker App  
#=======================================================================

import random
print("---Decision maker app---")
print("1.Coffee selector")
print("2. Dice roller")
choice = input("Enter your choice(1 or 2):")
if choice == "1":
    coffees=["Espresso","Macchinato","latte","cappuccino","americano"]
    selected = random.choice(coffees)
    print("you should try:",selected)
elif choice =="2":
    dice = random.randint(1,6)
    print("you rolled a :",dice) 
else:
    print("invalid choice! Please enter 1 or 2.")      