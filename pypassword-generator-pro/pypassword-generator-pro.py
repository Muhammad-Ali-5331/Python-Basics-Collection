import random

password_list = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '-', '_', '=', '¬', '<', '>', ':', ';' , '{', '}', '[', ']']

print("Welcome to the PyPassword Generator!\n")
nr_letters= int(input("\nNumber of Letters in Your Password = "))
nr_symbols = int(input(f"\nNumber of symbols in Your Password = "))
nr_numbers = int(input(f"\nHow many numbers should be in Your Password = "))

for lettter in range(0, nr_letters):
    index1 = random.randint(0, len(letters) - 1) #We Can also use random.choice() here!
    password_list += letters[index1]
for symbol in range(0, nr_symbols):
    index2 = random.randint(0, len(symbols) - 1)
    password_list += symbols[index2]
for number in range(0, nr_numbers):
    index3 = random.randint(0, len(numbers) - 1)
    password_list += numbers[index3]
#Method 1;
password_string_not_shuffled = ''.join(password_list) #converting list fromat of password to a single string without spaces/any character

#Method 2:
password = "" #Empty String
for char in password_list:
    password += char

#Method 1:
random.shuffle(password_list) #shuffling the list in place as suffle() returns nothing(create no new list)
password_string_shuffled = ''.join(password_list) #converting the shuffled list into a single string without spaces/any character

#Method 2:
#password_list_shuffled = random.sample(password_list, len(password_list)) #Getting a new list with shuffled elements
#password_string_shuffled = ''.join(password_list_shuffled) #Converting shuffled list to string

print(f"\nEasy Password = {password_string_not_shuffled}\nHard Password = {password_string_shuffled}")
