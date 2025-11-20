## 🔢 Number Word to Integer Converter

This script demonstrates a basic method for processing natural language strings that represent numbers and converting them into their final numerical integer value. It uses a dictionary lookup for number words and accumulates the total based on magnitude (hundreds, thousands, millions). 

## 🚀 How to Run

Run the script:
```bash
    python main.py
```
The script currently uses a hardcoded input: "One million two hundred thirty four thousand five hundred sixty seven".

It will print the original word string followed by the calculated numerical value (formatted with commas).

## 💡 Conversion Logic

The program uses the following approach to parse the input words:

<h3>Dictionary Mapping:</h3> All relevant words (one through ninety, and magnitude words like hundred, thousand, million) are mapped to their corresponding numerical values.

<h3>Accumulation:</h3> It uses two variables, current_value and total, to track the numbers within a single scale (e.g., the hundreds before a "thousand") and the final total:

1. Small Numbers (< 100): Added to current_value.

2. Multiplier Words (100, 1000, 1000000):

    1. If the multiplier is 100, it multiplies the current_value.

    2. If the multiplier is 1,000 or greater, it multiplies the current_value and then adds the entire result to the main total before resetting current_value to 0, handling the magnitude separation (e.g., separating millions from thousands).

## ⚠️ Known Limitations

1. The current logic assumes a specific order and structure in the input and does not handle:

2. The word "and" (e.g., "five hundred and sixty-seven").

3. Hyphenated numbers (e.g., "twenty-four").

4. The number zero.