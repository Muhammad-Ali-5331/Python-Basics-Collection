# 🪓 Hangman CLI Game

A classic word-guessing game built in Python, featuring modular graphics and a life-based difficulty system.

## Features
- **Modular Assets:** Separates game logic from ASCII art and word lists for better maintainability.
- **Intelligent Tracking:** Prevents users from losing lives on letters they've already guessed.
- **Visual Progression:** Displays evolving Hangman stages as the player runs out of attempts.
- **Dynamic Feedback:** Real-time updates to the word blanks and status messages for every guess.

## File Structure
- `main.py`: The primary game loop and logic.
- `mywordslist.py`: A collection of potential words for the game.
- `hangman_art_stages.py`: Contains the ASCII art for the various hangman lives.
- `arts.py`: Storage for the main project logo.

## How to Play
1. Ensure all supporting `.py` files are in the same directory.
2. Run `python main.py`.
3. Guess letters one by one. You have 7 lives—don't let the man hang!