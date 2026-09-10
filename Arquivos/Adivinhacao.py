import random
while True:
    num = random.randint(1, 10)
    print("Tente acertar o número de 1 a 10")
    tentativa = int(input())
    if num == tentativa:
        print("Você acertou!, o número era:", num)
        break
    else:
        num != tentativa
        print("Você errou, o número era:", num)
        
