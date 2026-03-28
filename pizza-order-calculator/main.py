pizza_size = input("What sie of Pizza you want? S,M,L = ")
add_pepproni = input("Want to add Pepproni to Pizza? Y or N = ")
add_cheese = input("Want to add cheese? Y or N = ")

print("\n")

bill = 0
if pizza_size == "S":
      bill = 15
      if add_pepproni == "Y":
          bill += 2
      if add_cheese == "Y":
          bill += 1
elif pizza_size == "M":
      bill = 20
      if add_pepproni == "Y":
          bill += 3
      if add_cheese == "Y":
          bill += 1
elif pizza_size == "L":
      bill = 25
      if add_pepproni == "Y":
          bill += 3
      if add_cheese == "Y":
          bill += 1
else:
      print("Wrong Input")
print(f"Your final bill is ${bill}")