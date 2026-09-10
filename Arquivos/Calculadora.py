while True:
    print("Digite a operação:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    operacao = int(input())
    print("Digite o primeiro número:")
    n1 = float(input())
    print("Digite o segundo número:")
    n2 = float(input())

    match ( operacao ):
        case 1:
            operacao = n1 + n2
            print("O resultado é:", operacao)
            break
        case 2:
            operacao = n1 - n2
            print("O resultado é:", operacao)
            break  
        case 3:
            operacao = n1 * n2
            print("O resultado é:", operacao)
            break  
        case 4:
            operacao = n1 / n2
            print("O resultado é:", operacao)
            break 
        case _:
            print("Digite a operação correta!!!")         
 