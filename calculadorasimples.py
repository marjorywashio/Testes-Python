print("------- VERIFICAÇÃO DE MAIORIDADE -------\n")

num1 = float(input("Primeiro número: "))
operacao = input("Operação(+ - / *): ")
num2 = float(input("Segundo número: "))

resultado = ''

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "/":
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = num1 / num2
elif operacao == "*":
    resultado = num1 * num2
else:
    print("Operação não encontrada. Repita o cálculo.")

if resultado != '':
    print(f"O resultado é {resultado}")

