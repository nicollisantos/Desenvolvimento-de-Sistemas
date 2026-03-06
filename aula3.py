# insira sua idade, em seguida, vamos usar uma estrutura de controle if-elife-else para verificar em qual faixa etária a pessoa se encontra.
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é adulto.")
else:
    print("Você é idoso.")