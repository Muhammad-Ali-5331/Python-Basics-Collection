## 🎯 Three Sum Algorithm (Two-Pointers)

This script provides an efficient solution to the Three Sum Problem, which is the task of finding all unique triplets $(a, b, c)$ in an array nums such that $a + b + c = 0$.

## 🚀 How to Run

Run the script:
```bash
    python main.py
```

The script will execute the threeSum method with the sample array [-2, 0, 1, 1, 2] and print the list of unique triplets that sum to zero.

## 💡 Algorithm Logic

The naive approach is $O(n^3)$, but this solution optimizes the process to achieve an $O(n^2)$ time complexity by using the following steps:

<b>Sorting:</b> The input array nums is first sorted. This is crucial as it allows us to control the target sum's value based on the position of our pointers.

<b>Outer Loop (Fixed Element):</b> The code iterates through the array with an index i (representing the first number, $a$). A check is included to skip duplicate values for $a$ to ensure uniqueness in the final result.

<b>Two-Pointers (Inner Search):</b> For each fixed element $n$ at index $i$, two pointers, left (starting at $i+1$) and right (starting at the end of the array), are used to find the remaining two numbers ($b$ and $c$).

1. If Sum is Zero: If $n + nums[\text{left}] + nums[\text{right}] = 0$, the triplet is added to the result. Both pointers are then moved inward, and additional checks are performed to skip any duplicate values at the new left position.

2. If Sum is Negative: If the sum is less than zero, the left pointer is moved right (left+=1) to increase the sum.

3. If Sum is Positive: If the sum is greater than zero, the right pointer is moved left (right-=1) to decrease the sum.

<b>Time Complexity:</b> $O(n^2)$ (dominated by the nested loops)

<b>Space Complexity:</b> $O(1)$ or $O(n)$ (depending on the sorting implementation's space usage)