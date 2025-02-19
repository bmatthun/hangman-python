import random
from hangmanpics import HANGMANPICS

counter = 0

while True:
    start_game = input('''Hey! Do you want to play a little Hangman?\n 
    Type YES (y) or NO (n): ''')
    if counter == 3:
        print("You has to be f#cking braindead.")
        break
    if start_game == "y" or start_game == "n":
        break
    else:
        print("Wrong input, try again!")
        counter += 1

if start_game == "n":
    print("\nMaybe next time! 👋")

else:
    playername = input("\nNice, then let's play! :)\n\nType your name: ")
    health = len(HANGMANPICS)
    hangman = ""
    game_over = False
    
    word_list = ["aardvark", "baboon", "camel"]
    word = random.choice(word_list)
    word_splitted = list(word)
    underscores = []
    already_guessed = []
    for letter in word_splitted:
        underscores.append("_")
    
    while (start_game == "y" and not game_over):
        print(f"\nYour word is: {underscores}")
    
        player_guess = input("\nTry and guess a letter: ")
    
        if len(HANGMANPICS) > health:
            hangman = HANGMANPICS[len(HANGMANPICS) - health]
            print(hangman)
    
        if player_guess in already_guessed:
            print("\nTry a new one, you already used this one.")
        elif player_guess in word_splitted:
            already_guessed.append(player_guess)
            print("\nWell done! Nice guess! :)")
            while player_guess in word_splitted:
                index_of_letter = word_splitted.index(player_guess)
                underscores[index_of_letter] = player_guess
                word_splitted[index_of_letter] = "_"
            print(f"{underscores}")
        else:
            already_guessed.append(player_guess)
            print("\nWrong guess! :/")
            health -= 1
            hangman = HANGMANPICS[len(HANGMANPICS) - health]
            print(health - 1)
            print(hangman)
            if health == 1:
                game_over = True
                print("\nYou lost! 😔😔😔")
    
        if "_" not in underscores:
            game_over = True
            print("\nYou won! 🎉🎉🎉")
            