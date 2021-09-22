
from cheesy_words import cheese
from logo import logo
from mechanics import get_word, blackout_solution, game_on, guess_word, refresh


print(logo)
print("🧀～The human-right compliant word-guessing game～🐁")

while game_on():
    refresh()
    print(
        "Guess the word and save your cheese wedge from Mousy the mouse!\n 🧀・・・・・・・🐁"
    )

    solution = get_word(cheese)
   
    guess = blackout_solution(solution)
   
    steps_to_the_cheese = 7
   
    refresh()
   
    guess_word(guess, solution, steps_to_the_cheese)
    
    refresh()
