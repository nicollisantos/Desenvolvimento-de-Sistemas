#Você foi contratado para criar o módulo de inventário de um novo jogo. O jogador deve ser capaz de adicionar quantos itens encontrar pelo caminho e só parar de organizar a mochila quando desejar.

inventario = []
while True:
    print(f'Sua lista está deste modo: {inventario}')
    entrada = input(" Você quer digitar o nome de um item encontrado no inventário ou sair? (Digitar/Sair) ").lower().strip()
    if entrada == "sair":
        print("Você se desconectou.")
        break
    elif entrada == "digitar":
        item = input("Digite o nome de um item encontrado no inventário: ").strip()
        inventario.append(item)
    else:
        item = print("Entrada inválida. ")

inventario.sort()
print("Inventário em ordem alfabética: ", inventario)
print("Quantidade de itens na lista: ", len(inventario))