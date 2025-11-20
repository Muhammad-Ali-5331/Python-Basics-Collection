## 🎯 Random Bill Payer Picker

This is a simple utility to randomly select one person from a group to pay for a shared meal or expense. It demonstrates two common ways to select a random element from a Python list.

## 🚀 How to Run

Run the script:
```bash
    python main.py
```

The program will prompt you to Enter The names separated by comma.

Example Input: Alice, Bob, Charlie, David

The name of the randomly selected person will be printed to the console.

## 💡 Selection Logic

The program uses two different methods from the random module to achieve the same result:

1. random.choice(list): Directly selects and returns a random item from the list.

2. random.randint(0, len-1): Generates a random integer index, which is then used to retrieve the element at that index (names[index]).

Both methods are shown in the script, resulting in the name being printed twice.