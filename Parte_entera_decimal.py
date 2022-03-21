import math

numero = 80.1265
print("El número es: ", numero)
parte_decimal, parte_entera = math.modf(numero)
print("Su parte entera es {:g} y su parte decimal es {:g}".format(
    parte_entera, parte_decimal))