tabuada = input("falae um numero: ")

contador = 0
limite = 10

for i in range(1, 12):
    resultado = int(tabuada) * contador
    if contador <= limite:
        print(tabuada, "x ", contador, " = ", resultado, "\n")
        contador += 1
