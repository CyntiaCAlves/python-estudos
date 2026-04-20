import random
alunos = []
for i in range(1, 5):
    nome = input("Digite o nome do {}º aluno: ".format(i))
    alunos.append(nome)
escolhido = random.choice(alunos)
print("-" * 30)
print("O aluno sorteado foi: {}".format(escolhido))
print("-" * 30)
