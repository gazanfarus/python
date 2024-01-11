import random
import hangman_art
import hangman_words
import os

clear = lambda: os.system('cls')

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
wrong_choices = []
for _ in range(word_length):
    display += "_"

lives = 6
while not end_of_game:
#    clear()
    guess = input("Guess a letter: ").lower()

    if guess in display or guess in wrong_choices:
      print("\nYou've already chosen this letter")

    if guess in chosen_word and not guess in display:
      print("\nNice!")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess in chosen_word or guess in wrong_choices:
      pass
    else:
      print("\nOh no, try again...")
      lives -= 1
      wrong_choices += guess
    print(hangman_art.stages[lives])

    print(f"{' '.join(display)}\n")
    print(f"Letters you've already chosen:\n{' '.join(wrong_choices)}\n")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")
    elif lives == 0:
      end_of_game = True
      print("\nYou've lost...")
