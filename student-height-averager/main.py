sum_heights = 0
t_s = 0

std_heights = input("Enter Heights of Students = ").split()

for n in std_heights:
    sum_heights += int(n)
    t_s += 1
print(f"\nAverage height of a Student = {round(sum_heights/t_s)}")

#Method 2:
#number_std = len(std_heights)
#sum-heights = sum(std_heights)
#print(f"\nAverage height of a Student = {round(sum_heights/number_std)}")