#     Exercício 4
# - Escreva um programa que solicita o nome de alunos e suas respectivas notas de 4 provas.
# Ao final, o programa deve imprimir o nome dos alunos e suas médias.

alunos = []
mediatotal = []
resp = 's'

while resp == 's':
    alunos.append(input("Digite o nome do aluno: "))
    total = 0

    for nota in range(4):
        nota = float(input("Digite a nota do aluno: "))
        total = total + nota

    media = total/4
    mediatotal.append((media))
    
    resp = input("Deseja adicionar outro aluno (s/n)? ")

print("\n========= MÉDIAS =========")

for aluno, nota in zip(alunos, mediatotal):
    print(f"{aluno} - Média: {nota}")
