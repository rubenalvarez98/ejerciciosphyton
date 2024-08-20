def cuadrados_ordenados(array, S):
    cuadrados_validos = []

    for numero in array:
        cuadrado = numero * numero
        if 0 <= cuadrado <= S**2:
            cuadrados_validos.append(cuadrado)


    def bubble_sort(lst):
        n = len(lst)

        for i in range(n):

            for j in range(0, n-i-1):

                if lst[j] > lst[j+1]:

                    lst[j], lst[j+1] = lst[j+1], lst[j]

        return lst

    return bubble_sort(cuadrados_validos)


entrada_1 = [1, 2, 3, 5, 6, 8, 9]
resultado_1 = cuadrados_ordenados(entrada_1, 7)
print(resultado_1)

entrada_2 = [-2, -1]
resultado_2 = cuadrados_ordenados(entrada_2, 7)
print(resultado_2)

entrada_3 = [-6, -5, 0, 5, 6]
resultado_3 = cuadrados_ordenados(entrada_3, 7)
print(resultado_3)

entrada_4 = [-10, 10]
resultado_4 = cuadrados_ordenados(entrada_4, 7)
print(resultado_4)



