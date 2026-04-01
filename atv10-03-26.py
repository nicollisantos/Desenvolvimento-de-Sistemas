#declaro lista

turma = ["Eduardo","Sophia","Nicolas","Lucas"]
print(turma)
novoNome = input("Adicione um novo nome dentro da turma: ")
turma.append(novoNome)
print()
print(turma)
print()
remover = input("Remova um ou mais alunos(as) da turma: ")
turma.remove(remover)
print()
print(f"Você removeu o(a/os/as) aluno(a/os/as): {remover} ")
print()
print("O número de alunos da turma atualmente é/são: ", len(turma))