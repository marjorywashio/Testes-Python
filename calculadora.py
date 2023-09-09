print("---------- Calculadora de Juros Simples ----------\n")

valor = float(input("Digite o valor principal: "))

juros = float(input("Digite a taxa de juros anual: "))

tempo = float(input("Digite o tempo em anos: "))

juros1 = juros/100

montante = valor + (valor * juros1 * tempo)

print("\n---------- Resultado ----------")
print(f"Com o valor principal de R${valor: .2f}, ao final de {tempo} anos, com juros de{juros: .2f}% ao ano, o montante total é de R${montante: .2f}")