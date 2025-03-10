import random
import hangman_art
import hangman_words

the_word = random.choice(hangman_words.word_list)
print(f"answer is {the_word}")
blanks_len = len(the_word)
display = []
for _ in range(blanks_len):
    display += "_"
print(hangman_art.logo)
print(" ".join(display))


def hangman():
    lives = 6
    continue_game = True
    while continue_game:
        user_choice = input("Guess a letter: ").lower()
        if user_choice in display:
            print(f"You have guessed {user_choice} already. Guess something else")
        for position in range(blanks_len):
            letter = the_word[position]
            if letter == user_choice:
                display[position] = letter

        print(" ".join(display))
        if user_choice not in display:
            print("Your guess in incorrect. You lose a life!")
            lives -= 1
            if lives == 0:
                continue_game = False
                print("Game Over, You ran out of lives!")
        if "_" not in display:
            print("You Win!")
            continue_game = False
        print(hangman_art.stages[lives])


hangman()
