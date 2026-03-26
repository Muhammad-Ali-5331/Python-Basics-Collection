from arts import ceaser_cipher_logo


def silent_auction(name, bid):
    bids[name] = bid


def highest_bidder():
    highest_bid = 0
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    print(f"\nThe highest bid is ${highest_bid} by {key}")


print(f"{ceaser_cipher_logo}\n")

bids = {}
choice = True
condition = True

while choice:
    user_name = input("\nEnter the Bidder name = ")
    user_bid = int(input("\nEnter Your Bid Price = $"))
    silent_auction(user_name, user_bid)
    while condition:
        continue_status = input("\nType 'yes' if there is another bidder otherwise type 'no': ").lower()
        if continue_status == "no" or continue_status == "yes":
            break
        else:
            print("\nWrong Input")
            continue
    if continue_status == "no":
        choice = False
        highest_bidder()
    elif continue_status == "yes":
        continue
    else:
        break