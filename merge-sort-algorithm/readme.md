## 🧩 Merge Sort Algorithm

This script provides an implementation of the Merge Sort algorithm  for sorting a list of integers in ascending order. This is a highly efficient, comparison-based sorting technique.

## 🚀 How to Run

Run the script:
```bash
  python main.py
```

The script will execute the MergeSort function with a sample array [9,8,7,6,5,4,3,2,1] and print the sorted result.

## 💡 Algorithm Logic (Divide and Conquer)

Merge Sort operates on the principle of Divide and Conquer:

<b>Divide</b>: The unsorted list is recursively divided into $N$ sublists, each containing one element (a list of one element is considered sorted).

<b>Conquer/Merge</b>: The sublists are then repeatedly merged to produce new sorted sublists until there is only one sorted list remaining. The core of the algorithm lies in the merge function, which efficiently combines two sorted lists into one.

<b>Time Complexity (Worst/Average/Best)</b>: $O(n \log n)$

<b>Space Complexity</b>: $O(n)$