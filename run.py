import random  # imports random library to pick a word randomly
from words import weird_words, welcome_banner  # imports weird word list and welcome_banner from words.py file


# function to randomly choose a word from weird words list
def pick_word():
    actual_word = random.choice(weird_words)
    return actual_word.upper()


def play_game(actual_word):
    word_reveal = "_" * len(actual_word)
    user_guessed = False
    user_guessed_letters = []
    user_guessed_words = []
    user_tries = 6
    print(welcome_banner)
    print("---------------------------------------------------- ")
    print("---------------------------------------------------- \n")
    print("This is Weird Word Hangman.")
    print("Your mission (should you wish to accept it)")
    print("is to try and guess the weird word!")
    print("Each underscore corresponds to a hidden letter.")
    print("If you input a correct guess, it will replace the underscore.")
    print("You have 6 lives. Go! Don't leave the man hanging! \n")
    print("---------------------------------------------------- ")
    print("---------------------------------------------------- \n")

    chars = "abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ"
    while True:
        user_name = input("What is your name? \n")
        if all(char in chars for char in user_name):
            break
        print("I'm sorry, this name is not valid! Please use only alphabet letters. \n")
    print("\n")
    print("Hi", user_name, "best of luck! \n")
    print("---------------------------------------------------")
    print("--------------------------------------------------- \n")

    print(show_hangman(user_tries))
    print(word_reveal)
    print("\n")
    while not user_guessed and user_tries > 0:
        user_guess = input("Please guess a word or letter:").upper()
        print("--------------------------------------------------- \n")
        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in user_guessed_letters:
                print("Sorry, but you've actually already guessed this letter!", user_guess)
            elif user_guess not in actual_word:
                print(user_guess, "is actually not in the word. :(")
                user_tries -= 1
                user_guessed_letters.append(user_guess)
            else:
                print("Nice one! ", user_guess, "is in the actual word!")
                user_guessed_letters.append(user_guess)
                guessed_word_as_list = list(word_reveal)
                indexes = [i for i, letter in enumerate(actual_word) if letter == user_guess]
                for index in indexes:
                    guessed_word_as_list[index] = user_guess
                word_reveal = "".join(guessed_word_as_list)
                if "_" not in word_reveal:
                    user_guessed = True
        elif len(user_guess) == len(actual_word) and user_guess.isalpha():
            if user_guess in user_guessed_words:
                print("You've actually already guessed the word!", user_guess)
            elif user_guess != actual_word:
                print(user_guess, "isn't the word I'm afraid :/")
                user_tries -= 1
                user_guessed_words.append(user_guess)
            else:
                user_guessed = True
                word_reveal = actual_word
        else:
            print("Sorry, this guess was invalid, please try again! :)")
        print(show_hangman(user_tries))
        print(f"{user_tries}, lives remaining")
        print(word_reveal)
        print("\n")
    if user_guessed:
        print("Nice one! You guessed the weird word =-O")
    else:
        print(f"The man has been hung ¯\_(ツ)_/¯, the hidden word was actually {actual_word}")


def show_hangman(user_tries):
    status = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return status[user_tries]


def main():
    actual_word = pick_word()
    play_game(actual_word)
    while input("Would you like to play again? (Y/N) ").upper() == "Y":
        actual_word = pick_word()
        play_game(actual_word)


if __name__ == "__main__":
    main()
