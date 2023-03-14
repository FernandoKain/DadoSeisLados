import random

def roll_dice():
    return random.randint(1, 6)

dice_faces = [
    "+-------+",
    "|       |",
    "|   O   |",
    "|       |",
    "+-------+"
]

def print_dice(number):
    print(dice_faces[0])
    for i in range(1, 4):
        line = dice_faces[i].replace("O", str(number))
        print(line)
    print(dice_faces[-1])

while True:
    user_input = input("Pressione enter para rolar o dado (ou q para sair)...")

    if user_input.lower() == 'q':
        break

    number = roll_dice()
    print_dice(number)
    print("O dado rolou e o número foi:", number)
    input("Pressione enter para jogar novamente...")

