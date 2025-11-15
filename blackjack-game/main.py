import random
from arts import blackjack_logo


def add_card_user():
    user.append(cards[random.randint(0, len(cards) - 1)])
    user_total = sum(user)
    return user_total


def add_dealer_card():
    dealer.append(cards[random.randint(0, len(cards) - 1)])
    dealer_total = sum(dealer)
    return dealer_total


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while 2 > 0:
    continue_status = input("\nDo you want to play a game of Blackjack? Type 'yes' or 'no': ").lower()
    if continue_status == "no":
        break
    elif continue_status == "yes":
        print(f"{blackjack_logo}")
        user = []
        dealer = []
        for _ in range(2):
            user.append(cards[random.randint(0, len(cards) - 1)])
            dealer.append(cards[random.randint(0, len(cards) - 1)])
        user_total = sum(user)
        dealer_total = sum(dealer)
        print(f"\nYour Cards: {user}, current score: {sum(user)}\nDealer's first card: {dealer[0]}")
        if user_total == 21:
            print("\nYou have a Blackjack! You have Won!")
            break
        elif dealer_total == 21:
            print("\nDealer has a Blackjack! You have Lost!")
            break
        while 2 > 0:
            choice = input("\nType 'hit' to get another card. Type 'stand' to pass: ").lower()
            new_user_total = user_total
            if choice == "hit":
                new_user_total = add_card_user()
                if new_user_total > 21:
                    print(f"\nYour Final Score: {new_user_total}. Your have crossed! You have lost!")
                    break
                else:
                    print(f"\nYour Cards: {user}, current score: {new_user_total}\nDealer's first card: {dealer[0]}")
            elif choice == "stand":
                new_dealer_total = dealer_total
                while new_dealer_total < 16:
                    new_dealer_total = add_dealer_card()
                if new_dealer_total > 21:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\nDealer Final hand: {dealer}, final score: {new_dealer_total}. Dealer have crossed!")
                    print("\nYou Have Won!")
                    break
                elif new_user_total > new_dealer_total:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\nDealer Final hand: {dealer}, final score: {new_dealer_total}")
                    print("\nYou have Won!")
                    break
                elif new_dealer_total > new_user_total:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\nDealer Final hand: {dealer}, final score: {new_dealer_total}")
                    print("\nDealer Won!")
                    break
                elif new_user_total == new_dealer_total:
                    print(
                        f"\nYour Final hand: {user}, final score: {user_total}\nDealer Final hand: {dealer}, final score: {new_dealer_total}")
                    print("\nThis is a Draw!")
                    break
                print("\n")
            else:
                print("\nWrong Input")
                continue
    else:
        print("\nWrong Input")
        continue

print("\n\t\tGood Bye, See You Next Time! ")