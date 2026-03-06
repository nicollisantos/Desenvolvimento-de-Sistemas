while True:
    opcao = int(input("Qual operação você deseja realizar?:" \
    "\n1 - soma \n2 - subtração\n3 - multiplicação" \
    "\n4 - divisão\n0 - sair\nEscolha de operação: ")) 

    if opcao == 1:
        print("------Adição------")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print()
        print(f"O resultado é: {soma}")

    elif opcao == 2:
        print("------Subtração------")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        subtração = num1 - num2
        print()
        print(f"O resultado é: {subtração}")

    elif opcao == 3:
        print("------Multiplicação------")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        multiplicação = num1 * num2
        print()
        print(f"O resultado é: {multiplicação}")

    elif opcao == 4:
        print("------Divisão------")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        divisão = num1 / num2
        print()
        print(f"O resultado é: {divisão}")
        
    elif opcao == 0:
        break

    else:
        print("------Esolha novamente------")
        continue