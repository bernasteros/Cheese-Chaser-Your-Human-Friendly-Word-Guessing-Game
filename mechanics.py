from time import sleep as slp
from random import choice
from os import system, name

def refresh():
    slp(1)
    clear()

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# Reads the Word-Database and Provides Selection Screen
def get_word(word_dict):
    difficulty = ""

    while difficulty not in word_dict:
        difficulty = input('''Please choose your Level!
      [e]asy
      [m]edium
      [h]ard
      
      >>> ''').lower()

        if difficulty not in word_dict:
            slp(1)
            print("\nPlease make a valid choice!\n")
            slp(1)
            clear()
    chosen_word = [letter for letter in choice(word_dict[difficulty])]
    return chosen_word


# Removes the letters to guess
def blackout_solution(solution):
    word_to_guess = ["_" for i in solution]
    return word_to_guess


# Checks whether guess and solution are identical
def guess_solution(guess, solve):
    return guess != solve


# Displays the current game progress
def show_screen(word_to_guess, steps):
    cheese = "🧀"
    mouse = "🐁"
    step = ""
    for s in range(steps):
        step = step + "・"

    mouse_path = cheese + step + mouse
    solution_screen = ' '.join(word_to_guess)

    print(f"{solution_screen}\n {mouse_path}")


# Used for starting or quitting the game
def game_on():
    print("\nStart a new round?")
    slp(1)
    run_game = input("Press 'Y' to start or any key to quit.\n\n >>> ").lower()
    if run_game == "y":
        return True
    else:
        print("Thank you for Playing :)\n Good Bye!")
        return False


# Controls inserting one letter at a time
def letter_input():
    guess = ""
    while len(guess) <= 0 or len(guess) > 1:
        guess = input("Please guess a letter: ").lower()
        if len(guess) <= 0:
            print("You have to guess a letter!")
            slp(2)
        elif len(guess) > 1:
            print("Calm down, just one letter at a time!")
            slp(2)
    return guess


# The game mechanic itself / uses functions above
def guess_word(word_to_guess, word_to_solve, life_count):
    while guess_solution(word_to_guess, word_to_solve):
        clear()
        show_screen(word_to_guess, life_count)
        guess = letter_input()

        for i in range(len(word_to_guess)):
            if word_to_solve[i] == guess:
                word_to_guess[i] = word_to_solve[i]

        if guess not in word_to_solve:
            life_count = life_count - 1
            if life_count == 0:
                clear()
                print("Oh noes!\n Mousy got the cheese!\n 💕🧀🐁💕")
                slp(3)
                print(f"The solution was {''.join(word_to_solve)}")
                break
            else:
                continue
    clear()
    show_screen(word_to_guess, life_count)
    if guess_solution(word_to_guess, word_to_solve):
        pass
    else:
        print(f"Congratulation, you found the solution :)")