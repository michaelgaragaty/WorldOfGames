import re
import GuessGame
import MemoryGame
import CurrencyRouletteGame
from Utils import screen_cleaner
from Score import add_score


def welcome(name):
    if name != '':
        print(f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.')
    else:
        while name == '':
            name = input("What is your name?")


def load_game():
    while True:
        games = input("""Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
           guess it back.
        2. Guess Game - guess a number and see if you chose like the computer.
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS.
    Enter your choice: """)

        if not re.match(r"^(?![1-3]$)|^$", games):
            break

    screen_cleaner()

    while True:
        difficulty = input('Please choose game difficulty from 1 to 5:')
        if not re.match(r"^(?![1-5]$)|^$", difficulty):
            break

    screen_cleaner()

    if games == '1':
        print(MemoryGame.play(int(difficulty)))
    elif games == '2':
        print(GuessGame.play(int(difficulty)))
    elif games == '3':
        print(CurrencyRouletteGame.play(int(difficulty)))
