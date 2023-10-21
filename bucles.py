'''
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.'''

for i in range(1,11):
    print(i)
    
x = 1
while x <= 20:
    if x % 2 == 0:
        print(x) 
    x +=1
    
suma = 0
for numero in range(1,101):
    suma += numero
print("La suma de los números del 1 al 110 es:", suma)