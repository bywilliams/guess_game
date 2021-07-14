import player
import random

p1 = player.Player
p2 = player.Player
p3 = player.Player

targetNumber = random.randint(0, 9)


def start_game():
    p1is_right = False
    p2is_right = False
    p3is_right = False

    p1guess: int
    p2guess: int
    p3guess: int

    while True:

        print("------------ Guess Game --------------")
        print("I'm thinking of a number between 0...9")
        print("Try to guess!")

        p1guess = int(input("Player 1º enter a number: "))
        p2guess = int(input("Player 2º enter a number: "))
        p3guess = int(input("Player 3º enter a number: "))
        p1.number1 = p1guess
        p2.number2 = p2guess
        p3.number3 = p3guess

        if p1.number1 == targetNumber:
            p1is_right = True
        if p2.number2 == targetNumber:
            p2is_right = True
        if p3.number3 == targetNumber:
            p3is_right = True

        if p1is_right or p2is_right or p3is_right:
            print(f" Player one tried to guess with the number: {p1.number1}")
            print(f" Player two tried to guess with the number: {p2.number2}")
            print(f" Player three tried to guess with the number: {p3.number3}")
            print("We have a winner!")
            print(f"Number to guess: {targetNumber}")
            print(f"Did player one get it right? {p1is_right}")
            print(f"Did player two get it right? {p2is_right}")
            print(f"Did player three get it right? {p3is_right}")
            break
        else:
            print("Players will have to try again, because no one got it right! \n")
