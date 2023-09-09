print("------- VERIFICAÇÃO DE MAIORIDADE -------\n")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação que deseja realizar: ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado é {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado é {resultado}")
elif operacao == "/":
    resultado = num1 / num2
    print(f"O resultado é {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado é {resultado}")
else:
    print("Operação não encontrada. Repita o cálculo.")

