from random import randint


def computerguess(lowerval, higherval, randnum, computer_count=0, firstiteration=True):
    if firstiteration:
        global computer_guess
        computer_guess = lowerval + (higherval + lowerval) // 2
        firstiteration = False
    if higherval >= lowerval:
        if computer_guess == randnum:
            return computer_count
        elif computer_guess > randnum:
            computer_count += 1
            computer_guess -= 1
            return computerguess(lowerval, computer_guess, randnum, computer_count, firstiteration=False)
        elif computer_guess < randnum:
            computer_count += 1
            computer_guess += 1
            return computerguess(computer_guess, higherval, randnum, computer_count, firstiteration=False)
    else:
        return False


user_required_range = input(
    "Enter Upper and Lower Range For Number Guessing (Enter Values Separated by Comma): ").split(",")
randnum = randint(int(user_required_range[0]), int(user_required_range[1]))
print(randnum)
guess = -1
computer_guess = 0
user_count = 0
firstIteration = True
while guess != randnum:
    if firstIteration:
        guess = int(input("Enter your Guess b/w 1 and 100: "))
        user_count += 1
        firstIteration = False
        continue
    if guess > randnum:
        print("Wrong! You Guessed Higher")
        guess = int(input("Enter your Guess b/w 1 and 100: "))
        user_count += 1
        continue
    elif guess < randnum:
        print("Wrong! You Guessed Lower")
        guess = int(input("Enter your Guess b/w 1 and 100: "))
        user_count += 1
        continue

print(f"Wow! You Guessed the Number in {user_count} steps")
print(
    f"Computer Took {computerguess(int(user_required_range[0]), int(user_required_range[1]), randnum)} steps to Guess!")