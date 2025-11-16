# 🧮 Console Chaining Calculator

A simple, interactive console application for performing basic arithmetic operations: addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).

## 🚀 How to Run

1.  Run the script:
    ```bash
    python main.py
    ```
2.  Follow the prompts to input the first and second numbers and the desired operation.
3.  After the initial calculation, you will be prompted to **continue** using the result or to exit.

## 💡 Functionality

* **Function Mapping:** Arithmetic operations are stored in a dictionary where the keys are the symbols (e.g., `+`) and the values are the corresponding Python functions.
* **Chaining:** The `calculations` function allows the user to take the previous result (`answer_1`) and use it as the first operand for the next calculation.