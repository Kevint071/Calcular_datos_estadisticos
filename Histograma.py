import matplotlib.pyplot as plot

lista = [11.5, 16.5, 17, 20, 21.5, 32, 25.5, 34.5, 19.5, 33, 23, 18.5, 19, 13.5, 35.5, 38, 32.5, 40, 28, 19.5, 30.5, 29, 33.5, 24.5, 27.5, 29.5, 16, 43.5, 24, 29, 28.5, 31, 15.5, 30, 35, 25, 30.5, 27, 41, 17.5, 34.5, 39.5, 26, 39, 32.5, 18, 26.5, 38, 37.5, 34.5, 33, 25.5, 46, 42, 22, 21, 35, 25.5, 30, 38.5, 17, 24.5, 22.5, 33.5, 37.5, 30, 43.5, 28.5, 30.5, 36, 26.5, 33.5, 27.5, 31.0, 38.5, 31.5, 26.5, 29, 22.5, 26, 20.5, 38.5, 34, 44, 28.5, 41.5, 27.5, 23, 23.5, 20.5, 29, 28, 32, 45.5, 18, 25, 37, 24.5, 35.5, 38.5]

intervalos = [11.45, 17.45, 23.45, 29.45, 35.45, 41.45, 47.45] #calculamos los extremos de los intervalos

print(intervalos)

plot.hist(x=lista, bins=intervalos, color='#F2AB6D', rwidth=0.95)
plot.title('Histograma de edades')
plot.xlabel('Edades')
plot.ylabel('Frecuencia')
plot.xticks(intervalos)

plot.show()