# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como 
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "E" (abaixo de 60).

nota = float(input("Digite uma nota de 0 a 100: "))
classificação = ''

if nota >=0 and nota <=100: 
    if nota >= 90:
        classificação = "A"
    elif nota >= 80 and nota <= 89:
        classificação = "B"
    elif nota >= 70 and nota <= 79:
        classificação = "C"
    elif nota >= 60 and nota <= 69:
        classificação = "D"
    else:
        classificação = "E"
    print(f"Classificação da nota: {classificação}")
else:
    print("Nota fora do parâmetro pedido (de 0 a 100)")

