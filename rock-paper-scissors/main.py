import random

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

#USER Sign/Choice:
user_choice = int(input("Write 0 for Rock, 1 for Paper and 2 for Scissors = "))

if user_choice == 0:
    user_sign = rock
elif user_choice == 1:
    user_sign = paper
elif user_choice == 2:
    user_sign = scissors
else:
    print("\nWrong Choice")

#COMPUTER Sign/Choice:
computer_choice = random.randint(0,2)

if computer_choice == 0:
    computer_sign = rock
elif computer_choice == 1:
    computer_sign = paper
elif computer_choice == 2:
    computer_sign = scissors

#Getting The Winner:

if user_choice == computer_choice: #Draw for being equal
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nThis is a Draw")
elif user_choice == 0 and computer_choice == 2: #Rock Fights Scissors
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nYou have Won!")
elif user_choice == 0 and computer_choice == 1: #Rock Fights Paper
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nYou have Lost!")
elif user_choice == 1 and computer_choice == 0: #Paper Fights Rock
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nYou have Won!")
elif user_choice == 1 and computer_choice == 2: #Paper Fights Scissors
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nYou have Lost!")
elif user_choice == 2 and computer_choice == 1: #Sciccors Fights Paper
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nYou have Won!")
elif user_choice == 2 and computer_choice == 0: #Scissors Fights Rock
    print(f"\nYour Choice:\n{user_sign}\nComputer Choice:\n{computer_sign}\nYou have Lost!")