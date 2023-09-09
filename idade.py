# Crie um programa que peça ao usuário para inserir sua idade e, em seguida, 
# informe se a pessoa é menor de idade ou maior de idade.

print("------- VERIFICAÇÃO DE MAIORIDADE -------\n")

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

