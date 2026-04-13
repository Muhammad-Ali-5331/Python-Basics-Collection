import random
from mywordslist import words_list
from hangman_art_stages import stages
from arts import hangman_logo

blanks = [] #blanks
chosen_word = random.choice(words_list) #It returns a string
word_length = len(chosen_word)

# Create Blanks:
for _ in range(word_length): # We use _ because this variable will not be used anywhere
    blanks.append(" _ ")

#print(f"Chosen Word = {chosen_word}")
print(f"{hangman_logo}")
print(f"\n{' '.join(blanks)}")

lives = 0
guessed_letters = []  # Track guessed letters

while " _ " in blanks:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed_letters:
        print(f"\nYou have already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)
    i = 0

    for letter in chosen_word:
        if letter == guess:
            blanks[i] = guess
        i += 1

    if guess in chosen_word:
        print(f"\nYou guessed '{guess}', that's a word. You saved Him! ✅")
    else:
        print(f"\n{stages[lives]}")
        lives += 1
        print(f"\nYou guessed '{guess}', that's not a word. You have lost a life ❎")

    print(f"\n{' '.join(blanks)}")

    if lives == 7:
        print("\nYou have lost all lives!")
        print(f"The word was: {chosen_word}")
        break

if lives < 7:
    print("\nYou have Won!")