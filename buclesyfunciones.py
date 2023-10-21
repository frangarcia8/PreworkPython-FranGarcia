'''
1. Crea una función para verificar si un número es par o impar y devuelva “El
número es par” o “El número es impar” según corresponda.
'''

def par_impar(numero):
    if numero % 2 == 0:
      return ("El número es par")
    else:
      return ("El número es impar")
numero = 11
resultado = par_impar(numero)
print(resultado)

'''
1. Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.'''

def factorial(numero):
    resultado = 1
    for i in range (1, numero+1):
      resultado *= i
    return resultado

num = int(input("Ingresa un número: "))
print("El factorial de ", num, "es: ", factorial(num))

'''
Crea una función a la que se le pase un número como argumento, calcule la
cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
'''

def contar_digitos(numero):
    return len(str(numero))

num = int(input("Ingresa un número: "))
print("La cantidad de dígitos es: ", contar_digitos(num))

'''
Dada una lista de números, crea una función que devuelva el número máximo
de la lista.
'''

def encontrar_maximo(lista):
    maximo = lista [0]
    for numero in lista:
      if numero > maximo:
          maximo = numero
    return maximo

numeros = [5, 12, 564, 8, 9]
print("El número máximo es:", encontrar_maximo(numeros))
  
'''Crea una función que, dado un número, sume los dígitos de ese número y
devuelva el resultado.'''

def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma
  
num = int(input("Introduce un número"))
print("La suma de los dígitos es:", suma_digitos(num))
