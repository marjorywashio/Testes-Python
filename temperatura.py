print("---------- Conversor de temperatura ----------\n")

celsius = float(input("Digite a temperatura em Celsius: "))

kelvin = celsius + 273

fahrenheit = (celsius * 9 / 5) + 32

print(f"A temperatura {celsius}ºC é de:")
print(f"{kelvin} K e de {fahrenheit}ºF")
