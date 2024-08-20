def reorganizar_y_filtrar(numeros, S):

    numeros_filtrados = []


    for numero in numeros:

        numero_str = str(numero)
        numero_filtrado_str = ""


        for caracter_digito in numero_str:

            digito = int(caracter_digito)


            if digito < S:
                numero_filtrado_str += caracter_digito


        if numero_filtrado_str:
            numeros_filtrados.append(int(numero_filtrado_str))


    n = len(numeros_filtrados)
    for i in range(n):
        for j in range(0, n-i-1):

            if numeros_filtrados[j] < numeros_filtrados[j+1]:
                numeros_filtrados[j], numeros_filtrados[j+1] = numeros_filtrados[j+1], numeros_filtrados[j]


    return numeros_filtrados

# Ejemplos de prueba
print(reorganizar_y_filtrar([1, 2, 3, 4, 5, 6,7], 7))
print(reorganizar_y_filtrar([10, 20, 30, 40], 7))
print(reorganizar_y_filtrar([6], 7))
print(reorganizar_y_filtrar([77], 7))
print(reorganizar_y_filtrar([65], 7))
print(reorganizar_y_filtrar([6, 2, 1], 7))
print(reorganizar_y_filtrar([60, 6, 5, 4, 3, 2, 7, 7, 29, 1], 7))

