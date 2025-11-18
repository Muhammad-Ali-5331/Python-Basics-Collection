# 🌀 Turtle Spirograph Generator

This script uses the Python **Turtle Graphics** module to generate complex, colorful, and symmetric patterns known as **spirographs** 

[Image of a spirograph pattern]
.

## 🚀 How to Run

1.  Run the script:
    ```bash
    python main.py
    ```
2.  A new window will open and the pattern will be drawn automatically. The window will close when clicked.

## 💡 Implementation Details

The core of the spirograph is created by **repeatedly drawing a circle** and then **rotating the turtle's direction** before drawing the next circle.

### Key Features:

* **Random Colors:** The `change_turtle_appearance()` function assigns a new random RGB color (using `colormode(255)`) to the pen before drawing each circle, resulting in a vibrant output.
* **Rotation Method:** The code achieves the rotation either by using `my_turtle.setheading(my_turtle.heading() + size_of_gap)` or by using `my_turtle.left(angle)`.
* **Speed:** The turtle's speed is set to a high value (`20` or `"fastest"`) to quickly render the complex pattern.