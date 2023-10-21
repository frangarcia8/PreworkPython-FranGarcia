'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''
print("Ingresa un número: ")
numero = int(input())

if (numero > 0):
    print("El número es positivo.")
elif (numero < 0):
    print("El número es negativo.")
else:
    print("El número es 0")
    
if (numero % 2 == 0 ):
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")



