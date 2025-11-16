weight = int(input("Enter your Weight in Kg = "))
height = float(input("\nEnter your Height in m = "))

#BMI stands for Body Mass Index

bmi = weight/height**2 #Formula to calculate BMI
#bmi = round(weight/height**2,2)

print("\n")

#Method 2:
if bmi < 18.5:
    print(f"Your BMI is {round(bmi,2)}, you are underweight")
elif 18.5 < bmi < 25:
    print(f"Your BMI is {round(bmi,2)}, you have normal weight")
elif 25 < bmi < 30:
    print(f"Your BMI is {round(bmi,2)}, you are overweight")
elif 30 < bmi < 35:
    print(f"Your BMI is {round(bmi,2)}, you are obese")
else:
    print(f"Your BMI is {round(bmi,2)}, you are clinically obese")

#Method 2:
# if bmi < 18.5:
#   print(f"Your BMI is {round(bmi,2)}, you are underweight")
# elif bmi < 25:
#   print(f"Your BMI is {round(bmi,2)}, you have normal weight")
# elif bmi < 30:
#   print(f"Your BMI is {round(bmi,2)}, you are overweight")
# elif bmi < 35:
#   print(f"Your BMI is {round(bmi,2)}, you are obese")
# else:
#   print(f"Your BMI is {round(bmi,2)}, you are clinically obese")