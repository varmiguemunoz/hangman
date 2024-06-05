"""
Entry point ⚡️
"""

import random
import os

from utils.hangman_pics import hangman_pics
from utils.database import database

def run():
    word = random.choice(database)
    spaces =["_"] * len(word)
    tries = 6

    print("iniciando el juego")

    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")

        print(hangman_pics[tries])
        letter = input("Elige una letra: ")

        found = False

        for index, character in enumerate(word):
            if character == letter:
                spaces[index] = letter
                found = True


        if not found:
            tries -= 1

        if "_" not in spaces:
            os.system("clear")
            print(f"¡Ganaste el juego! La palabra es: {word}")
            break

        if tries == 0:
            os.system("clear")
            print(f"¡Perdiste! La palabra era: {word}")
            break



if __name__ == "__main__":
    run()
