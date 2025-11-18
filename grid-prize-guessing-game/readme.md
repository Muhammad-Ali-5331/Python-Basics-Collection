## 🎁 Grid Prize Guessing Game

This is a simple console game where the user tries to guess the location of a hidden prize (🚗) on a 3x3 grid.

## 🚀 How to Play

Run the script:

```bash
    python main.py
```


The board is displayed. You must guess the position by entering two digits: Column (1-3) followed immediately by Row (1-3).

Example Input: Entering 13 means Column 1, Row 3.

Example Input: Entering 31 means Column 3, Row 1.

The board is then displayed again, showing either your success (🚗) or your failed guess (☠) and the location of the prize.

## 💡 Gameplay and Logic

The board is initialized with 🎁 emojis.

The prize location is determined randomly using random.randint(0,2).

The user's input (a two-digit string) is mapped to the zero-indexed board for checking.