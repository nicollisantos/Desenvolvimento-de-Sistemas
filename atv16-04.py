# CRUD Simples de Alunos (Python)

alunos = []

def create(nome, idade):
    alunos.append({'nome': nome, 'idade': idade})

def read():
    for aluno in alunos:
        print(aluno)
 
def update (indice, nome, idade):
    alunos [indice]['nome'] = nome
    alunos [indice]['idade'] = idade
 
def delete(indice):
    alunos.pop(indice)

# Exemplo de Uso

create("Ana", 20)
create("Bruno", 22)
read()
update(0, "Ana Clara", 21)
read()
delete(1)
read()