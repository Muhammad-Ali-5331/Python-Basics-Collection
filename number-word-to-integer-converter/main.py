user_input = "One million two hundred thirty four thousand five hundred sixty seven"
inp = user_input.strip().lower().split()
words = {
    "one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,
    "eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,
    "twenty":20,"thirty":30,"fourty":40,"fifety":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,
    "hundred":100,"thousand":1000,"hundred-thousand":100000,"million":1000000,"billion":1000000000,"trillion":1000000000000
}
current_value = 0
total = 0

for string in inp:
    if string in words:
        value = words[string]
        if value < 100:
            current_value += value
            #print(current_value)
        elif value == 100:
            current_value *= value
            #print(current_value)
        else:
            current_value *= value
            #print(current_value)
            total += current_value
            #print(total)
            current_value = 0

total += current_value
print(f"{user_input}:")
print("{:,}".format(total))