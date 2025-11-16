total_bill = float(input("Enter the Total Bill = $"))
number_of_people = int(input("Number of people to split the bill = "))
percentage_of_tip = float(input("Percentage Tip you like to pay = "))

bill_to_pay = (total_bill * (percentage_of_tip/100) + total_bill)/number_of_people #Example: =(124.56 * 0.12 + 124.56)/7 ------> 19.93
#bill_to_pay = (total_bill * (1 + percentage_of_tip/100))/number_of_people

print("Each person should pay: ", round(bill_to_pay,2))