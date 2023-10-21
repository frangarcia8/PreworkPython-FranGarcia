'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Define una función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''

def suma(a, b):
    return(a + b)
resultado = suma(4,5)
print(resultado)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
resultado = factorial(6)
print(resultado)

def es_primo(num):
    contador = 0
    for i in range(1, num+1):
        if num % i == 0:
            contador +=1
    if contador == 2:
            return True
    else:
            return False
print(es_primo(11))

def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

mi_lista = [1, 2, 3, 4, 5]
numeros = mi_lista
print(suma_lista(mi_lista))

def cadena_invertida(cadena):
    cadena_invertida = cadena[::-1]
    return(cadena_invertida)
cadena = "Principe"
print(cadena_invertida(cadena))

    


     

