print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You are on junction of road. Where do you want to go? Left or Right = ").lower()

if direction == "left": #Method to compare strings
    choice1 = input("You went to a lake. Do you want to Swim or Wait for boat = ").lower()
    if choice1 == "wait for boat":
        choice2 = input("You have 3 doors White, Blue, Red. One of them will save your life. Carefully chose one = ").lower()
        if choice2 == "white":
            print("Great Choice. One wise choice saved your life.")
        elif choice2 == "blue":
            print("Bad Choice. Lion ate you!")
        elif choice2 == "red":
            print("You fell from a height and Died!")
        else:
            print("Wrong Choice. Game Over!")
    else:
        print("You were eaten by a Shark. Game over!")
else:
    print("You got a car accident. Game Over!")