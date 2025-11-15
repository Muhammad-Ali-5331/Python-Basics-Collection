# 🐢 Turtle Geometric Shapes Generator

This Python script utilizes the built-in `turtle` graphics library to visually generate a sequence of regular geometric polygons, each rendered in a random color.

It serves as a simple demonstration of fundamental geometric drawing using the Turtle module.

## 📁 Directory

`turtle-geometric-shapes`

## ✨ Features

* **Dynamic Shape Generation:** Draws polygons starting from a triangle (3 sides) up to a decagon (10 sides).
* **Color Randomization:** Assigns a random pen color to each new shape drawn from a predefined list.
* **Simple Logic:** Uses a single function to calculate the necessary internal angle ($360^\circ / N$) for any regular polygon.

## 🛠️ Requirements

This script only requires the standard Python installation; it uses the `turtle` and `random` modules, which are part of the standard library.

## 🚀 How to Run

1.  **Save the file:** Save the code as a Python file (e.g., `main.py`) inside the `turtle-geometric-shapes` directory.


2.  **Execute:** Run the script from your terminal:

    ```bash
    python main.py
    ```

3.  **View:** A new window will open, displaying the turtle drawing the shapes sequentially. The window will close when you click on it.

## 📜 Code Snippet

```python
import random
from turtle import Turtle, Screen

# ... (rest of your code)