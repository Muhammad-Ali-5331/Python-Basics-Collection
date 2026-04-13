# 🔐 PyPassword Generator

A robust command-line utility for generating secure, customizable passwords with varying degrees of complexity.

## Features
- **Custom Entropy:** Choose the exact count of letters, numbers, and symbols required for your security policy.
- **Dual Output Modes:**
    - **Easy Mode:** Characters are added in the order requested (Letters -> Symbols -> Numbers).
    - **Hard Mode:** Characters are completely randomized using an in-place shuffle algorithm for maximum security.
- **Extended Symbols:** Includes a wide range of special characters (including brackets and math symbols) to defeat brute-force attacks.

## How It Works
1. **Selection:** The script pulls random characters from defined lists based on your counts.
2. **Collection:** It aggregates these into a single list.
3. **Randomization:** It uses `random.shuffle()` to ensure no predictable patterns exist in the "Hard" version.

## Usage
1. Run `python main.py`.
2. Enter the quantity for each character type.
3. Copy the "Hard Password" for maximum account security.