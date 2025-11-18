import random

row1 = ["🎁", "🎁", "🎁"]
row2 = ["🎁", "🎁", "🎁"]
row3 = ["🎁", "🎁", "🎁"]
board = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")

real_vertical_pos = random.randint(0,2)
real_horizontal_pos = random.randint(0,2)
real_pos_gift = str(real_vertical_pos) + str(real_horizontal_pos)

position = input("Guess the Postion of the Prize = ")

vertical_pos = int(position[0])
horizontal_pos = int(position[1])
user_given_pos = str(vertical_pos) + str(horizontal_pos)


if real_pos_gift == user_given_pos:
    selected_row = board[horizontal_pos - 1]
    selected_row[vertical_pos - 1] = "🚗"
    print(f"{row1}\n{row2}\n{row3}\n\nYou Won the prize!")
else:
    selected_row = board[horizontal_pos - 1]
    selected_row[vertical_pos - 1] = "☠"
    real_row = board[real_horizontal_pos - 1]
    real_row[real_vertical_pos - 1] = "🚗"
    print(f"{row1}\n{row2}\n{row3}\n\nYou Lost!")