def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def calculations(answer_1):
    for _ in operations:
        print(f"\n{_}")
    selected_operation = input("\nSelect an Operation from the above:")
    num3 = float(input("\nEnter next number = "))
    answer_2 = operations[selected_operation](answer_1, num3)
    print(f"\n{answer_1} {selected_operation} {num3} = {answer_2}")


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
num1 = float(input("\nEnter first number = "))

for key, value in operations.items():
    print(f"\nKey:{key}, Value:{value}, Type:{type(value)}")

selected_operation = input("\nSelect an Operation from the above:")
num2 = float(input("\nEnter second number = "))

answer_1 = operations[selected_operation](num1, num2)

print(f"\n{num1} {selected_operation} {num2} = {answer_1}")

while 2 > 0:
    print(f"\nType 'yes' if you want to continue calculation with {answer_1} or type 'no' to exit: ")
    continue_status = input("")
    if continue_status == "no":
        break
    elif continue_status == "yes":
        calculations(answer_1)
    else:
        print("\nWrong Input")
        continue