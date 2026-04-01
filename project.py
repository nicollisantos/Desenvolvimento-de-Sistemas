idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade. Não está apto para fazer aulas de autoescola.")
elif idade == 18:
    print("Você tem 18 anos, já está apto para fazer suas aulas de autoescola!")
elif idade > 18:
    print("Você é maior de idade, já está mais que apto para começar com a autoescola com  nossa empresa! =)")
else:
    print("Algo deu errado. Digite sua idade com números.")