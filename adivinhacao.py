from random import randint

#      Exercício 3
# - Escreva um programa que sorteia um valor de 1 a 100. O jogador pode então tentar acertar o valor,
# sendo que o programa informará se o chute é maior ou menor que o valor sorteado.
# O processo se repete até que o jogador acerte o valor sorteado.
# - Refatore o código para que ao final, mostre quantas tentativas foram necessárias para acertar.

numero = randint(1,10)
tentativa = 1

print("Adivinhe o número sorteado, de 0 a 100")
chute = int(input("Chute: "))

while numero != chute:
    if chute > numero:
        print("O número é menor. Tente novamente")
    else:
        print("O número é maior. Tente novamente")
    chute = int(input("Chute: ")) 
    tentativa += 1

if numero == chute:
    print("\n=======================")
    print("Parabéns! Você acertou!")
    print(f"Tentativas: {tentativa}")