#Presentación 
print(".*+ ¡Bienvenido al calculador de palabras distintas formables con letras repetidas! +*.")

#Opciones de entrada
print("Opciones de entrada:")
print("1. Ingresar una palabra o cadena")
print("2. Ingresar una lista de cantidades (n1, n2, ..., nk)")
opcion = input("Seleccione 1 o 2: ")

#Validación de opción
while opcion not in ["1", "2"]:
    print("Opción inválida! Por favor ingrese 1 para palabra o 2 para lista de cantidades")
    opcion = input("Seleccione 1 o 2: ")

opcion = int(opcion)

print()

#Función factorial
def factorial(x):
    f = 1
    i = x
    while i > 1:
        f = f*i
        i = i-1
    return f

#Caso 1: palabra
if opcion == 1:
    palabra = input("Ingrese la palabra o cadena: ").upper()
    while len(palabra) == 0:
        print("La palabra no puede estar vacía! Ingrese al menos una letra")
        palabra = input("Ingrese la palabra o cadena: ").upper()
    n = len(palabra)
    nfact = factorial(n)
    letras = {}
    for letra in palabra:
        if letra in letras:
            letras[letra] = letras[letra] + 1
        else:
            letras[letra] = 1
    denom = 1
    for cantidad in letras.values():
        denom = denom * factorial(cantidad)
    resultado = nfact // denom
    print("La cantidad de palabras distintas que se pueden formar con",palabra,"es:",resultado)

#Caso 2: lista de cantidades
else:
    entrada = input("¿Cuántos tipos de letras diferentes hay?: ")
    while not entrada.isdigit() or int(entrada) < 1:
        print("Debe ingresar un número entero positivo mayor que 0.")
        entrada = input("¿Cuántos tipos de letras diferentes hay?: ")
    k = int(entrada)

    cantidades = []
    i = 0
    while i < k:
        c = input("Ingrese la cantidad de la letra: ")
        #Validación: debe ser un número entero positivo (no cero, no negativo)
        while not c.isdigit() or int(c) <= 0:
            if c == "0":
                print("La cantidad no puede ser cero! Por favor ingrese un número válido (entero positivo mayor que 0)")
            else:
                print("La cantidad debe ser un número entero positivo mayor que 0")
            c = input("Ingrese la cantidad de la letra: ")
        c = int(c)
        cantidades = cantidades + [c]
        i = i+1

    n = sum(cantidades)
    nfact = factorial(n)
    denom = 1
    for c in cantidades:
        denom = denom * factorial(c)
    resultado = nfact // denom
    print("La cantidad de cadenas distintas que se pueden formar con las cantidades dadas es:",resultado)

print()

print(".*+ ¡Gracias por usar el calculador de palabras distintas con letras repetidas! +*.")
print("Fin del programa.")
