#Desenvolver um algoritmo que automatize o cálculo de médias escolares, permitindo a inserção de um número ilimitado de notas e fornecendo o status final do aluno.

#nivel 0 

notas = int(input("Digite a sua quantidade de notas que deseja adicionar: "))
somaDasnotas = []

while True:
    for i in range(notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        somaDasnotas.append(nota)

    media = sum(somaDasnotas) / len(somaDasnotas)
    print(f"Suas notas são: {somaDasnotas} \n"
    f"Sua média é {media:.2f}")

    if media < 0:
        print(f"Digite notas positivas.")
        break
    elif media < 7:
        print(f"SITUAÇÃO: REPROVADO")
        break    
    else:
        print(f"SITUAÇÃO: APROVADO")
        break