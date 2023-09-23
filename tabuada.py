#      Exercício 2 - Tabuada
# - Escreva o código para imprimir a tabuada do 2 usando um laço for
# - Refatore o código para solicitar ao usuário qual tabuada deve ser impressa

numero = int(input("Qual tabuada deseja imprimir? "))

print("========== FOR ===========")
for i in range (1,11):
    total = numero * i
    print(f"{numero} x {i} = {total}")

print("\n========= WHILE ==========")

i = 1
while i <= 10:
    total = numero * i
    print(f"{numero} x {i} = {total}")
    i += 1