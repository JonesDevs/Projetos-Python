while True:
    print("Digite a temperatura")
    temperatura = float(input())
    print("Deseja fazer qual conversão?\n1 - Farenheint\n2 - Celcius")
    escolha = int(input())
    match ( escolha ):
        case 1:
            conversaoFaren = (temperatura - 32) / 1.8
            print("A conversão é: ", conversaoFaren)
            break
        case 2:
            conversaoCelci = (temperatura * 1.8) + 32
            print("A conversão é:", conversaoCelci)
            break
        case _:
            print("Insira um tipo válido!!!")