def cambio_minimo(coins):

    coins.sort()


    cambio_min = 1


    for moneda in coins:

        if moneda <= cambio_min:

            cambio_min += moneda
        else:

            break

    return cambio_min



monedas1 = [5, 7, 1, 1, 2, 3, 22]

resultado1 = cambio_minimo(monedas1)
print(f"El cambio mínimo es: {resultado1}")

monedas2 = [1, 1, 1, 1, 1]

resultado2 = cambio_minimo(monedas2)
print(f"El cambio mínimo es: {resultado2}")

monedas3 = [1, 5, 1, 1, 1, 10, 15, 20, 100]

resultado3 = cambio_minimo(monedas3)
print(f"El cambio mínimo es: {resultado3}")
