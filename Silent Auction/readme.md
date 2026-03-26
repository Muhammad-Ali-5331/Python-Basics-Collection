# 🏛️ Silent Auction Engine

A streamlined, console-based bidding application designed for "blind" auctions. This program allows multiple users to enter their bids privately, stores the data securely in a local session, and calculates the winner once the bidding period concludes.

---

## 🚀 Features

- **Anonymous Bidding:** Individual bids are stored in a dictionary, ensuring others cannot see the current high bid during the entry phase.
- **Input Validation:** Built-in logic to handle user input errors, ensuring the session only continues or ends with valid "yes" or "no" commands.
- **Winner Determination:** A dedicated algorithm iterates through all participants to find the highest bidder and displays the final result automatically.
- **Visual Branding:** Includes a custom ASCII art interface for a professional command-line experience.

---

## 🛠️ Technical Stack

- **Language:** Python 3.x
- **Data Structure:** Dictionary-based mapping for $O(1)$ average-case insertion.
- **Modular Design:** Utilizes a separate `arts` module for UI elements to keep core logic clean and readable.

---

## 📖 How to Use

1. **Start the Script:** Run the program in your terminal.
2. **Enter Details:** Input your name and your bid price (numeric values only).
3. **Add More Bidders:** Type `yes` to clear the logic for the next person, or `no` to finish.
4. **View Results:** The program will instantly calculate and display the highest bid and the name of the winner.

---

## 📂 File Structure

* `main.py`: Contains the primary auction logic and loops.
* `arts.py`: Storage for the Caesar Cipher/Auction branding logo.