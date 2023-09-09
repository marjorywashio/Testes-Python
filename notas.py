# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como 
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "E" (abaixo de 60).

nota = float(input("Digite uma nota de 0 a 100: "))

if nota > 90:
    print("Classificação da nota: A")
elif nota > 80 and nota < 89:
    print("Classificação da nota: B")
elif nota > 70 and nota < 79:
    print("Classificação da nota: C")
elif nota > 60 and nota < 69:
    print("Classificação da nota: D")
elif nota < 60:
    print("Classificação da nota: E")