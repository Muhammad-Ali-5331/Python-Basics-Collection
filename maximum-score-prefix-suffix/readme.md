# 📈 Maximum Score Calculator

An efficient Python solution for calculating the maximum possible score from an array by leveraging precomputed prefix and suffix values.

## Features
- **Linear Time Complexity:** Processes the data in $O(n)$ time by avoiding nested loops.
- **Prefix Sums:** Tracks cumulative values to simplify score derivation.
- **Suffix Minimums:** Dynamically identifies the smallest trailing values to maximize the score difference.
- **Negative Integer Support:** Designed to handle negative number sets (e.g., `[-7, -5]`) using proper mathematical initialization.

## How it Works
The algorithm splits the problem into two distinct phases:
1. **Preprocessing:** It builds a running total from the left and a "running minimum" from the right.
2. **Evaluation:** It iterates through the split points to find where the `prefix[i] - suffix[i+1]` reaches its maximum value.

## Usage
1. Provide an array of integers to the `maximumScore` method.
2. The function returns the highest calculated score based on the array's internal distribution.