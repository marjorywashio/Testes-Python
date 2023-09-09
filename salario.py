# Peça ao usuário para inserir seu salário e o tempo de serviço. 
# Se o tempo de serviço for superior a 5 anos, conceda um bônus de 5% ao salário.

salario = float(input("Informe o salário: "))

tempo = float(input("Informe o tempo de serviço: "))

if tempo >= 5:
    salario = salario*1.05
    print(f"\nO salário acrescido de um bônus de 5% é de: {salario}")
else:
    print("\nNão houve alteração no salário")