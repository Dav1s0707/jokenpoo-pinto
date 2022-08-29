import random

while True:
    num = random.randint(1, 3)

    jog = int(input("""JOKENPO!!
    Digite 1 para pedra
    Digite 2 para papel
    Digite 3 para tesoura
    """))


    if num == 1:
        if jog >= 4 or jog <= 0:
            print("Digite um valor valido")
        else:
            print("Bot: 💎")

            if jog == 1:
                print("Voce:💎")
                print("EMPATE")
            elif jog == 2:
                print("Voce:📜")
                print("VOCE GANHOU!!!")

            elif jog == 3:
                print("Voce: ✂")
                print("VOCE PERDEU!!!")
            else:
                print("Digite um valor valido")

    elif num == 2:
        if jog >= 4 or jog <= 0:
            print("Digite um valor valido")
        else:
            print("Bot: 📜")
            if jog == 1:
                print("Voce: 💎")
                print("VOCE PERDEU!!!")
            elif jog == 2:
                print("Voce: 📜")
                print("EMPATE")
            elif jog == 3:
                print("Voce: ✂")
                print("VOCE GANHOU!!!")
            else:
                print("Digite um valor valido")

    elif num == 3:
        if jog >= 4 or jog <= 0:
            print("Digite um valor valido")
        else:
            print("Bot:✂")
            if jog == 1:
                print("Voce:💎")
                print("VOCE GANHOU!!!")
            elif jog == 2:
                print("Voce:📜")
                print("VOCE PERDEU!!!")
            elif jog == 3:
                print("Voce:✂")
                print("EMPATE")

    print("======="*20)