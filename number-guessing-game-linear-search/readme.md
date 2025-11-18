# 🔢 Number Guessing Game & AI Comparison

This script hosts an interactive console game where the user attempts to guess a random number. It then compares the user's performance (steps taken) against a computer AI's attempt to find the same number.

## 🚀 How to Run

1.  Run the script:
    ```bash
    python main.py
    ```
2.  **Set the Range:** Enter the lower and upper bounds for the random number, separated by a comma (e.g., `1,100`).
3.  **User Guesses:** Follow the prompts to enter your guesses.
4.  **Results:** The program will report your total guesses and the computer's total guesses.

## 🧠 Computer Guessing Strategy

The `computerguess` function attempts to solve the problem using a hybrid, but mostly **linear-progression** strategy:

1.  **Initial Guess:** It starts at the average of the low and high range.
2.  **Sequential Search:** It then moves **one step at a time** (+1 or -1) from that starting point towards the target number until it is found. This makes its efficiency comparable to a slow linear search in most cases.