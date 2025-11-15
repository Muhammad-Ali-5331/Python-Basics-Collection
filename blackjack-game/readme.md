# 🃏 Python Blackjack Game

A console-based simulation of the classic card game, Blackjack (or 21).

## 🚀 How to Play

1. Ensure you have an `arts.py` file containing the `blackjack_logo` string (or remove the line `from arts import blackjack_logo`).


2. Run the script:
    ```bash
    python main.py
    ```
   
3. Follow the prompts to start a new game, 'hit' to take another card, or 'stand' to end your turn.

## 💡 Game Rules Implemented

* Initial deal of two cards to the player and dealer.
* Aces (`11`) currently count as 11, with no logic to change to 1.
* Dealer must 'hit' (take another card) if their total is less than 16.
* Checks for initial Blackjack (21) for both player and dealer.
* Determines winner based on score (closest to 21 without going over).