## 📌 Insertion Sort Algorithm

This script provides an implementation of the Insertion Sort algorithm  for sorting a list of integers in ascending order. It's an efficient algorithm for small data sets or data sets that are already substantially sorted.

## 🚀 How to Run

Run the script:
```bash
    python main.py
```
The script will execute the insertionSort function with a sample array [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] and print the sorted result.

💡 Algorithm Logic

The Insertion Sort algorithm works like sorting a hand of playing cards:

It iterates through the array starting from the second element.

The current_value is pulled out.

The algorithm scans backward through the sorted portion (elements to the left) and shifts all elements greater than current_value one position to the right.

Finally, current_value is placed into the empty spot, inserting it into the correct position.

Time Complexity (Worst/Average): $O(n^2)$

Time Complexity (Best): $O(n)$ (when the list is already sorted)