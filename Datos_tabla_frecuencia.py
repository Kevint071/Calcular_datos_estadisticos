from math import *
import pandas as pd
import matplotlib.pyplot as plot

lista = [11.5, 16.5, 17, 20, 21.5, 32, 25.5, 34.5, 19.5, 33, 23, 18.5, 19, 13.5, 35.5, 38, 32.5, 40, 28, 19.5, 30.5, 29, 33.5, 24.5, 27.5, 29.5, 16, 43.5, 24, 29, 28.5, 31, 15.5, 30, 35, 25, 30.5, 27, 41, 17.5, 34.5, 39.5, 26, 39, 32.5, 18, 26.5, 38, 37.5, 34.5, 33, 25.5, 46, 42, 22, 21, 35, 25.5, 30, 38.5, 17, 24.5, 22.5, 33.5, 37.5, 30, 43.5, 28.5, 30.5, 36, 26.5, 33.5, 27.5, 31.0, 38.5, 31.5, 26.5, 29, 22.5, 26, 20.5, 38.5, 34, 44, 28.5, 41.5, 27.5, 23, 23.5, 20.5, 29, 28, 32, 45.5, 18, 25, 37, 24.5, 35.5, 38.5]

decimal_mayor = 0

for i in range(0, len(lista)):
    if i == 0:
        parte_decimal, parte_entera = modf(lista[i])
        mayor_decimal = parte_decimal
        mayor_decimal = (f"{mayor_decimal:g}")

    if i > 0:
        parte_decimal, parte_entera = modf(lista[i])


        parte_decimal = (f"{parte_decimal:g}")

        if len(parte_decimal)-2 >= len(mayor_decimal) -2:
            mayor_decimal = parte_decimal
            decimal_mayor = len(mayor_decimal) -2
        
        if decimal_mayor < 0:
            decimal_mayor = 0

print("\nNumero de decimales: ", decimal_mayor)

if decimal_mayor == 0:
    division = 0.5
else:
    division = float("0." + ("0"*(decimal_mayor-1)) + "1")/2
print(f"Punto medio de cada unidad de medida: {division}")

rango = max(lista) - min(lista)
print(f"\nRango: {max(lista)} - {min(lista)} =", rango)

limite_superior = max(lista) + division
limite_inferior = min(lista) - division

print(f"\nLimite superior: {limite_superior}")
print(f"Limite inferior: {limite_inferior}\n")

m = ceil(1 + (3.3 * log(len(lista), 10)))

print(log(len(lista), 10))

print(f"m: {1 + (3.3 * log(len(lista), 10)):g} = {m}")

c = ceil(rango/m)

print(f"C: {rango/m} = {c}")

lista_intervalos = []

intervalos = limite_inferior

for i in range(m+1):
    if i == 0:
        intervalos = round(intervalos, decimal_mayor + 1)
        lista_intervalos.append(intervalos)
    else:
        intervalos = round(intervalos, decimal_mayor + 1) + c
        lista_intervalos.append(intervalos)

if lista_intervalos[-2] > limite_superior:
    lista_intervalos.pop(-1)

print(f"\nLista intervalos: {lista_intervalos}\n")

intervalos_inferiores = lista_intervalos[:-1:]
intervalos_superiores = lista_intervalos[1::]

print(f"Intervalos inferiores: {intervalos_inferiores}")
print(f"Intervalos superiores: {intervalos_superiores}")

frecuencia_absoluta = []

for inferior, superior in zip(intervalos_inferiores, intervalos_superiores):
    contador = 0
    for z in lista:
        if z > inferior and z < superior:
            contador = contador + 1
    frecuencia_absoluta.append(contador)

frecuencia_absoluta_acumulada = []

acum = 0

for i in frecuencia_absoluta:
    acum = acum + i
    frecuencia_absoluta_acumulada.append(acum)

print(f"\nFrecuencia absoluta: {frecuencia_absoluta}")
print(f"Frecuencia absoluta acumulada: {frecuencia_absoluta_acumulada}")
print(f"Sumatoria: {sum(frecuencia_absoluta)}")

frecuencia_relativa = []

for i in frecuencia_absoluta:
    frecuencia_relativa.append(round(i/sum(frecuencia_absoluta), 3))

frecuencia_relativa_acumulada = []

acum = 0

for i in frecuencia_relativa:
    acum = acum + i
    frecuencia_relativa_acumulada.append(round(acum, 2))

print(f"\nFrecuencia relativa: {frecuencia_relativa}")
print(f"Frecuencia relativa acumulada: {frecuencia_relativa_acumulada}")
print(f"Sumatoria: {round(sum(frecuencia_relativa), 3)}")

xi = []

for inferior, superior in zip(intervalos_inferiores, intervalos_superiores):
    xi.append((superior + inferior)/2)

print(f"\nMarca de clase acumulada: {round(sum(xi), 2)}")

xifi = []

for i, j in zip(xi, frecuencia_absoluta):
    xifi.append(round(i*j, 2))

x = sum(xifi)/sum(frecuencia_absoluta)
print(f"\nMedia: {round(x, 2)}")

xi_x = []

for i in xi:
    xi_x.append(abs(round(i - x, 3)))

print(f"\n∑ xifi: {round(sum(xifi), 2)}")
print(f"∑ xi - x: {round(sum(xi_x), 3)}")

xi_x_2 = []

for i in xi_x:
    xi_x_2.append(round(i**2, 3))

print(f"∑ (xi - x)2: {round(sum(xi_x_2), 2)}")

xi_x_2_fi = []

for i, j in zip(xi_x_2, frecuencia_absoluta):
    xi_x_2_fi.append(round(i * j, 2))

print(f"∑ (xi - x)2fi: {round(sum(xi_x_2_fi), 2)}\n")

da = {"lf": intervalos_inferiores, "ls": intervalos_superiores, "|": "|", "xi": xi, "fi": frecuencia_absoluta, "Fi": frecuencia_absoluta_acumulada, "hi": frecuencia_relativa, "Hi": frecuencia_relativa_acumulada, "xifi": xifi, "xi - x": xi_x, "(xi - x)2": xi_x_2, "(xi - x)2fi": xi_x_2_fi}

tabla = pd.DataFrame(data=da)
print(tabla)

intervalos = lista_intervalos

plot.hist(x=lista, bins=intervalos, color='#F2AB6D', rwidth=0.95)
plot.title('Histograma de edades')
plot.xlabel('Edades')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)

plot.show()