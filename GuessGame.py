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

        print("------------ Jogo da Advinhação --------------")
        print("Estou pensando em um número entre 0 e 9 ....")
        print("Tentem adivinhar!")

        p1guess = int(input("Jogador 1º digite um numero: "))
        p2guess = int(input("Jogador 2º digite um numero: "))
        p3guess = int(input("Jogador 2º digite um numero: "))
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
            print(f" jogador um forneceu o palpite: {p1.number1}")
            print(f" jogador dois forneceu o palpite: {p2.number2}")
            print(f" jogador três forneceu o palpite: {p3.number3}")
            print("Temos um vencedor!")
            print(f"Numero a adivinhar: {targetNumber}")
            print(f"O jogador um acertou? {p1is_right}")
            print(f"O jogador dois acertou? {p2is_right}")
            print(f"O jogador três acertou? {p3is_right}")
            break
        else:
            print("Os jogadores terão que tentar novamente, pois ninguém acertou! \n")
