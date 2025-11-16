# 🫧 Bubble Sort Algorithm

This script provides an implementation of the **Bubble Sort** algorithm 

[Image of bubble sort process]
 for sorting a list of integers in ascending order.

## 🚀 How to Run

1.  Run the script:
    ```bash
    python main.py
    ```
2.  The script will execute the `bubbleSort` function with a sample array `[9,8,7,6,5,4,3,2,1]` and print the sorted result `[1,2,3,4,5,6,7,8,9]`.

## 💡 Algorithm Features

* **Comparison Sort:** Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
* **Optimization:** Includes a flag (`swappingOuccurred`) to detect if a pass resulted in zero swaps. If no swaps occur, the list is sorted, and the outer loop terminates early.
* **Time Complexity (Worst/Average):** $O(n^2)$