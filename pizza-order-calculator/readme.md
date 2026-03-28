# 🍕 Pizza Order Calculator

A lightweight Python CLI application designed to automate the billing process for a pizza parlor based on size and custom toppings.

## Features
- **Flexible Sizing:** Supports Small (S), Medium (M), and Large (L) base prices.
- **Dynamic Surcharges:** Automatically adjusts topping costs (Pepperoni) based on the selected pizza size.
- **Additive Billing:** Calculates a cumulative total for multiple selections including extra cheese.
- **Instant Invoicing:** Provides a clear, formatted final price to the customer upon completion.

## Pricing Grid
| Item | Small (S) | Medium (M) | Large (L) |
| :--- | :--- | :--- | :--- |
| **Base Pizza** | $15 | $20 | $25 |
| **Pepperoni** | +$2 | +$3 | +$3 |
| **Extra Cheese**| +$1 | +$1 | +$1 |

## Usage
1. Run `python main.py`.
2. Follow the on-screen prompts (using S, M, L, Y, or N).
3. View your total calculated bill instantly.