import random

name_string = input("Enter The names sperated by comma: ")
names = name_string.split(", ")
names_len = len(names)

payer = random.choice(names)
print(f"\n{payer} is going to pay for the meal today")

index = random.randint(0,names_len - 1)
payer = names[index]

print(f"\n{payer} is going to pay for the meal today")