numero = 0

#while numero < 5:
#    numero += 1
#    print(numero)

#for numero in [1, 2, 3, 4, 5]:
#    print(numero)

#for numero in [1,2,3,4,5,6,7,8,9,10]:
#    print(numero)

#     Exercício 1 - Impressão de números
# - Escreve um programa que imprima números de 1 a 10 usando o laço for
# - Refatore o código para solicitar um número máximo para impressão ao usuário
# - Refatore o código para solicitar ao usuário se deve ser impresso em ordem crescente ou descrescente
numero = maximo = int(input("Até qual número você gostaria de imprimir? "))
ordem = int(input("Gostaria de ordenar de forma crescente (1) ou decrescente (2)? "))

if ordem == 1:
    for numero in range(1, maximo + 1):
        print(numero)
elif ordem == 2:
    for numero in range (maximo, 0, -1):
        print(numero)
else:
    print("\nEscolha a ordenação com os números 1 ou 2")

print("==========WHILE============")

if ordem == 1:
    numero = 1
    while numero <= maximo:
        print(numero)
        numero +=1
elif ordem == 2:
    while maximo > 0:
        print(maximo)
        maximo -= 1
else:
    print("\nEscolha a ordenação com os números 1 ou 2")