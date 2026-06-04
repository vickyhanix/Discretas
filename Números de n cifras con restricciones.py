#Presentación 
print(".*+ ¡Bienvenido al calculador de números de distintas cifras! +*.")

#Pedimos al usuario que ingrese el número de cifras n para el número
entrada = input("¿Qué número de cifras deberá tener el número?: ")

#Validación: debe ser un número entero positivo mayor que 0
while not entrada.lstrip('-').isdigit() or int(entrada) < 1:
    n = int(entrada) if entrada.lstrip('-').isdigit() else -1
    if n == 0: 
        #Comentario: caso especial cuando n = 0
        print("Es imposible crear números sin cifras! Por favor ingrese un número válido (entero positivo mayor que 0)")
    elif n < 0:
        #Comentario: caso especial cuando n es negativo
        print("El número de cifras debe ser positivo! Por favor ingrese un número válido (entero positivo mayor que 0)")
    else:
        print("Debe ingresar un número entero positivo mayor que 0.")
    entrada = input("¿Qué número de cifras deberá tener el número?: ")

n = int(entrada)

print()

#Cálculo de números de n cifras sin repetir dígitos
if n > 10: 
    print("Si el número es mayor que 10, es imposible que no se repitan dígitos")
    sr = 0
elif n == 1: 
    sr = 9 #Si solo es 1 cifra hay 9 alternativas (sin 0)
else: 
    i = n
    a = 9 #Para la primera cifra hay 9 alternativas (no puede ser 0)
    sr = 9
    while i > 1:
        sr = sr*a #Para la segunda 9, luego 8, 7...
        a = a-1
        i = i-1
print("La cantidad de números de",n,"cifras sin repetir dígitos es:",sr)

print()

#Cálculo de números pares de n cifras sin repetir dígitos
if n > 10: 
    print("Si el número de cifras es mayor que 10, es imposible hallar pares sin que se repitan dígitos")
    par = 0
elif n == 1:
    par = 4 #2,4,6,8
    print("La cantidad de números pares de 1 cifra sin repetir dígitos es:",par)
else:
    par = 0
    ultimos = [0,2,4,6,8]
    j = 0
    while j < 5:
        u = ultimos[j]
        if u == 0:
            primeros = 9
            a = 9
        else:
            primeros = 8
            a = 8
        temp = primeros
        i = n-2
        while i > 0:
            temp = temp*a
            a = a-1
            i = i-1
        par = par + temp
        j = j + 1
    print("La cantidad de números pares de",n,"cifras sin repetir dígitos es:",par)

print()

#Cálculo de números de n cifras que empiezan con un dígito dado
print("Ahora vamos a calcular los números que empiezan con un dígito específico")
entrada = input("Ingrese el dígito inicial: ")
while not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 9:
    print("El dígito inicial debe estar entre 1 y 9. Por favor ingrese otro dígito")
    entrada = input("Ingrese el dígito inicial: ")
inicio = int(entrada)

calcinicio = 1
i = n-1
while i > 0:
    calcinicio = calcinicio*10
    i = i-1
print("La cantidad de números de",n,"cifras que empiezan con",inicio,"es:",calcinicio)

print()

#Cálculo de números de n cifras que contienen al menos un cero
if n > 10:
    print("Si el número de cifras es mayor que 10, es imposible que no se repitan dígitos")
    con0 = 0
elif n == 1:
    con0 = 0
else:
    total = sr
    sin0 = 9
    a = 8
    i = n-1
    while i > 0:
        sin0 = sin0*a
        a = a-1
        i = i-1
    con0 = total - sin0
    print("La cantidad de números de",n,"cifras que contienen al menos un cero es:",con0)

print()

#Cálculo de números de n cifras formados con un conjunto de dígitos elegido por el usuario
entrada = input("¿Cuántos dígitos quiere ingresar para el conjunto?: ")
while not entrada.isdigit() or int(entrada) < 1:
    print("Debe ingresar al menos un dígito para formar números")
    entrada = input("¿Cuántos dígitos quiere ingresar para el conjunto?: ")
cantdigitos = int(entrada)

digitos = []
i = 0
while i < cantdigitos:
    entrada = input("Ingrese un dígito (0–9): ")
    while not entrada.isdigit() or int(entrada) < 0 or int(entrada) > 9:
        print("Debe ingresar un dígito válido entre 0 y 9")
        entrada = input("Ingrese un dígito (0–9): ")
    d = int(entrada)
    digitos = digitos + [d]
    i = i + 1

digitos = list(set(digitos))

if digitos == [0]:
    print("No se pueden formar números porque el único dígito ingresado es 0")
    calcset = 0
else:
    if 0 in digitos:
        primeros = len(digitos) - 1
    else:
        primeros = len(digitos)

    calcset = primeros
    i = n-1
    while i > 0:
        calcset = calcset * len(digitos)
        i = i - 1

    print("La cantidad de números de",n,"cifras formados con el conjunto dado es:",calcset)

print()
print(".*+ ¡Gracias por usar el calculador de números de distintas cifras! +*.")
print("Fin del programa.")
