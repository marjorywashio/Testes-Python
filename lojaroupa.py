print("---------- LOJA DE ROUPAS ----------")

compra = float(input("\nInforme o valor total da compra: "))

print("\nv: à vista | p: a prazo")
pagamento = input("Qual a forma de pagamento? ")

if pagamento == "v":
    if compra <= 500:
        total = (compra*0.90) #10% de desconto
        print(f"O total da compra é R${total: .2f}")
    if compra > 500 and compra < 1000:
        total = compra*0.85 #15% de desconto
        print(f"O total da compra é R${total: .2f}")
    if compra >= 1000:
        total = compra*0.80 #20% de desconto
        print(f"O total da compra é R${total: .2f}")

if pagamento =="p":
    if compra <= 800:
        print("\nA compra pode ser parcelada em até 4x")
        parcelas = int(input("Gostaria de parcelar em quantas vezes? "))
        if parcelas <= 4:
            total = compra / parcelas
            print(f"\nCompra parcelada em {parcelas} vezes de R${total: .2f}")
        else:
            print("A compra pode ser parcelada em no máximo 4x!")
    if compra > 800:
        print("\nA compra pode ser parcelada em até 18x")
        print("----- Até 10x sem juros -----")
        parcelas = int(input("\nGostaria de parcelar em quantas vezes? "))
        if parcelas < 11:
            total = compra/parcelas
            print(f"Compra parcelada em {parcelas} vezes de R${total: .2f} sem juros")
        if parcelas == 11:
            juros = 0.05
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 12:
            juros = 0.065
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 13:
            juros = 0.07
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 14:
            juros = 0.09
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 15:
            juros = 0.095
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 16:
            juros = 0.1
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 17:
            juros = 0.113
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        elif parcelas == 18:
            juros = 0.12
            total = compra + (compra * juros * parcelas)
            print(f"\nCompra parcelada em {parcelas} vezes de R${total/parcelas: .2f}")
        else:
            print("\nA compra pode ser parcelada em até 18x")