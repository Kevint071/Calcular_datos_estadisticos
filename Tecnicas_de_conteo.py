from math import factorial

titulo = "Bienvenido al sistema de técnicas de conteo de estadística"
print("                    " + titulo.center(76, "-"))

while True:
    try:
        #Se pide si importa el orden de los elementos
        orden = int(input("Digite si importa el orden si(1), no(2): "))
        
        if orden == 1:

            while True:
                try:
                    #Se pide si se utilizan todos los elementos
                    utilizan = int(input("Digite si se utilizan todos los elementos si(1) no(2): "))

                    if utilizan == 1:
                        
                        abecedario = "abcdefghijklmnñopqrstuvwxyz"
                        lista_abecedario = lista_abecedario.split("")
                        
                        #Se usan después para quitar las tildes a la palabra que se va a digitar si el usuario desea digitar la palabra 
                        tilde, no_tilde = 'áäéëíïóöúüÁÉËÍÏÓÖÚÜ','aaeeiioouuAEEIIOOUU'
                        conversion = str.maketrans(tilde, no_tilde)

                        print("\nLo que quiere hallar es una permutacion\n")
                        
                        repeticion = int(input("Digite si hay repetición si(1), no(2): "))

                        if repeticion == 1:
                            print("\nLa fórmula de la permutacion es: PR = n! / a!b!c!\n")
                            while True:
                                try:
                                    si_no = int(input("¿Desea digitar una palabra para este tipo de permutación? 1(si) 2(no): "))
                                    if si_no == 1:
                                        palabra = input("Digite la palabra: ")
                                        palabra = palabra.lower()
                                        
                                        #Aquí ya se utiliza la conversión de la palabra quitando las tildes a la palabra digitada
                                        palabra = palabra.translate(conversion)

                                        cantidad_letras = len(palabra)

                                        lista_repeticion = []
                                        lista_letras = []
                                        
                                        #Este ciclo sirve para añadir las veces que se repite una letra en la palabra digitada a la lista llamada lista_repeticion y además añade la letra que se repitió a una lista llamada lista_letras
                                        for i in range(0, len(abecedario)):
                                            veces = palabra.count(abecedario[i])
                                            
                                            if veces >= 2:
                                                lista_repeticion.append(veces)
                                                lista_letras.append(abecedario[i])
                                        print()
                                        if not 2 in lista_repeticion:
                                            print("No hay letras repetidas")
                                            print(f"La formula quedaría PR = {cantidad_letras}!")
                                        
                                        elif sum(lista_repeticion)/len(lista_repeticion) != 1:
                                                    
                                            for i in range(0, len(lista_repeticion)):
                                                print(f"La letra {lista_letras[i]} tiene {lista_repeticion[i]} repeticiones")

                                            print(f"\nLa formula quedaría PR = {cantidad_letras}! / ", end = "")

                                            for i in range(0, len(lista_repeticion)):
                                                if i != len(lista_repeticion)-1:
                                                    print(f"{lista_repeticion[i]}! x", end = " ")
                                                else:
                                                    print(f"{lista_repeticion[i]}!", end = "")

                                        factorial_denominador = 1

                                        for i in range(0, len(lista_repeticion)):
                                            factorial_denominador *= factorial(lista_repeticion[i])
                                            
                                        factorial_numerador = factorial(cantidad_letras)
                                        resultado = factorial_numerador/factorial_denominador

                                        if resultado % 1 == 0:
                                            resultado = int(resultado)
                                        else:
                                            resultado = (f"{resultado:g}")
                                            resultado = float(resultado)

                                        print(f"\nEl resultado de la permutacion es {resultado}")
                                        break
                                    
                                    elif si_no == 2:                                        
                                        while True: 
                                            try:
                                                ejemplo = int(input("\n¿Desea ver un ejemplo para contestar lo siguiente? 1(si) 2(no): "))
                                                
                                                if ejemplo == 1:
                                                    print("""
                                                        Ejemplo para contestar las preguntas de permutación:
                                                        
                                                        ¿Cuantos elementos hay en la palabra 'holamama'(n)?
                                                        Rta = 8
                                                        
                                                        ¿Cuantos elementos repetidos hay en la palabra 'holamama'?
                                                        Rta = 2
                                                        
                                                        Esos dos elementos son a y m
                                                        
                                                        La a tiene 3 elementos repetidos en esa palabra
                                                        La m tiene 2 elementos repetidos en esa palabra
                                                        
                                                        Digite los elementos repetidos del elemento 1 osea la letra 'a': 3
                                                        Digite los elementos repetidos del elemento 2 osea la letra 'm': 2""")
                                                    break
                                                elif ejemplo == 2:
                                                    break
                                                else:
                                                    print("Número no válido\n")
                                            except:
                                                print("Número no válido○\n")
                                        while True:
                                            n = int(input("\nDigite la cantidad de elementos (n) de su palabra: "))                                        
                                            repetir_abc = int(input("\n¿Cuantos elementos repetidos hay en su palabra?: "))
                                            
                                            lista_elementos_repetidos = []
                                            print()
                                            for i in range(1, repetir_abc+1):
                                                elemento_repetido = input(f"Digite cuantos elementos repetidos hay del elemento {i}: ")
                                                lista_elementos_repetidos.append(elemento_repetido)
                                            
                                            lista_factorial_elementos = list(map(lambda x: factorial(int(x)), lista_elementos_repetidos))
                                            lista_elementos_repetidos = list(map(lambda x: int(x), lista_elementos_repetidos))
                                            lista_elementos_repetidos = list(filter(lambda x: True if x > 1 else False, lista_elementos_repetidos))
                                            lista_factorial_elementos = list(filter(lambda x: True if x > 1 else False, lista_factorial_elementos))
                                            
                                            if sum(lista_elementos_repetidos) > n:
                                                print("No puede haber mas elementos repetidos que la cantidad total de elementos")
                                            else:
                                                break
                                        
                                        print(f"\nLa formula quedaría PR = {n}! / ", end = "")
                                        
                                        for i in range(0, len(lista_elementos_repetidos)):
                                            if i != len(lista_elementos_repetidos)-1:
                                                print(f"{lista_elementos_repetidos[i]}! x", end = " ")
                                            else:
                                                print(f"{lista_elementos_repetidos[i]}!", end = "")
                                        
                                        factorial_numerador = factorial(n)
                                        
                                        acum = 1
                                        
                                        for i in lista_factorial_elementos:
                                            acum = acum * i
                                        factorial_denominador = acum
                                        
                                        resultado = factorial_numerador/factorial_denominador
                                        
                                        if resultado % 1 == 0:
                                            resultado = int(resultado)
                                        else:
                                            resultado = (f"{resultado:g}")
                                            resultado = float(resultado)
                                        
                                        print(f"\nEl resultado de la permutacion es {resultado}")
                                        break
                                except:
                                    print("El valor no es válido\n")                    
                        elif repeticion == 2:
                            break
                        else:
                            print("El número no es válido\n")
                        break
                    
                    elif utilizan == 2:
                        print("\nLo que quiere hallar es una variación\n")
                        
                        while True:
                            repeticion = int(input("Digite si hay repetición si(1), no(2): "))
                            if repeticion == 1 or repeticion == 2:
                                break
                            else:
                                print("Número no válido\n")
                        
                        while True:
                            try:
                                n = int(input("\nDigite el número de elementos que hay (n): "))
                                k = int(input("Digite la cantidad de elementos que se utilizan (k): "))
                            
                                if k > n:
                                    print("El número de elementos usados(k) debe ser menor o igual a la cantidad total de elementos(n)")
                                else:
                                    if repeticion == 1:
                                        
                                        print("\nLa fórmula de la variación es: V = n!/(n-k)!")
                                        print(f"\nLa fórmula quedaría V = {n}! / ({n}-{k})!\n")
                                                            
                                        resta_n_k = n-k
                                        resultado = factorial(n)/(factorial(resta_n_k))
                                                            
                                        print(f"El resultado de la variación es: {resultado:g}")
                                        break
                                    elif repeticion == 2:
                                        
                                        print("\nLa fórmula de la variación es: V = n**k")
                                        print(" "*31 + "V = n^k")
                                        print(f"\nLa fórmula quedaría V = {n}**{k}")
                                        print(" "*20 + f"V = {n} ^ {k}\n")
                                        
                                        resultado = n**k
                                                           
                                        print(f"El resultado de la variación es: {resultado}")
                                        break
                                    else:
                                        print("El número no es válido\n")
                            except:
                                print("Valor no válido\n")
                        break
                    else:
                        print("El número no es válido\n")
                except:
                    print("El valor no es válido\n")
            break
        elif orden ==2:
            print("\nLo que quiere hallar es una combinación\n")
            
            while True:
                try:
                    n = int(input("Digite el número de elementos que hay (n): "))
                    k = int(input("Digite la cantidad de elementos que se utilizan (k): "))
                    if k > n:
                        print("\nEl número de elementos usados(k) debe ser menor o igual a la cantidad total de elementos(n)")
                    else:
                        break
                except:
                    print("Valor no válido")
                    
            while True:
                try:
                    repo = int(input("Digite si la extracción se realiza con reposicion si(1), no(2): "))
                    if repo == 1:
                        print("\nLa fórmula es C = n! / (n-k)!k!")
                        print(f"\nLa fórmula quedaría C = {n}! / ({n}-{k})!{k}!\n")
                                    
                        resta_n_k = n-k
                        resultado = factorial(n)/(factorial(resta_n_k) * factorial(k))
                                    
                        print(f"El resultado de la combinación es: {resultado:g}")
                        break
                    elif repo == 2:
                        print("\nLa fórmula es C = (n + k - 1)! / k!(n - 1)!")
                        print(f"\nLa fórmula quedaría C = ({n} + {k} - 1)! / {k}!({n} - 1)!")
                        print(f"\n                    C = {n + k - 1}! / {k}!{n - 1}!\n")

                        resultado = factorial(n + k - 1)/(factorial(k) * factorial(n - 1))
                        
                        print(f"El resultado de la combinación es: {resultado:g}")
                        break
                    else:
                        print("Número no válido\n")
                except:
                    print("Valor no válido\n")
            break
        else:
            print("El número ingresado no es válido\n")
    except:
        print("El valor no es válido\n")