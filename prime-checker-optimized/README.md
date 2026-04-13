# 🔢 Optimized Prime Checker

A high-performance primality testing utility that leverages mathematical properties to determine if a number is prime with maximum efficiency.

## Features
- **Square Root Pruning:** Drastically reduces iterations by only checking divisors up to the square root of the target number.
- **Early Exit Strategy:** Instantly filters out non-prime even numbers and multiples of three before entering the main loop.
- **Efficient Iteration:** Skips even divisors within the search loop to halve the computational load.
- **Clean Interface:** Uses a functional approach that can be easily imported into other mathematical projects.

## Technical Insight
By only checking up to $\sqrt{n}$, this script can handle much larger integers than a naive $O(n)$ trial division approach. For example, to check if $2099$ is prime, it only needs to test divisors up to $\approx 45$.

## Usage
1. Open `main.py`.
2. Set the variable `n` to any integer you wish to test.
3. Run: `python main.py`.