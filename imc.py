print("Seja bem vindo(a)!! \n")

nome = input("Qual é o seu nome? ")

idade = int(input("Qual é a sua idade? ")) #converter para inteiro

peso = float(input("Qual é o seu peso? ")) #converter para float

altura = float(input("Qual é a sua altura? ")) #converter para float

imc = peso/(altura*altura)

print(f"Olá {nome}!")
print(f"Sua idade é de {idade} anos.")
print(f"Seu IMC é de:{imc: .2f}.")