import random

print(" ****** DICE ROLLING SIMULATOR ******** ")
roll_dice = "y"

while roll_dice=="y":
    #to generate a random dice number from 1 to 6
    dice_number = random.randint(1,6)

    if dice_number==1:
        print("----------")
        print("|        |")
        print("|   0    |")
        print("|        |")
        print("----------")
        

    if dice_number==2:
        print("----------")
        print("|        |")
        print("|  0  0  |")
        print("|        |")
        print("----------")

    if dice_number==3:
        print("----------")
        print("| 0      |")
        print("|    0   |")
        print("|       0|")
        print("----------")

    if dice_number==4:
        print("----------")
        print("| 0    0 |")
        print("|        |")
        print("| 0    0 |")
        print("----------")

    if dice_number==5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")

    if dice_number==6:
        print("-----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("-----------")

    x = input("Press y to roll again : ")
else:
    print("\n\n***** THANK YOU ******")
    
        
