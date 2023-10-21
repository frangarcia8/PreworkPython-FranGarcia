'''Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.'''

def contador_letras(palabra):
    contador = 0
    for letra in palabra:
      if letra.isalpha():
        contador +=1
    return contador
      
palabra = input ("Introduce una palabra: ")
print (("La cantidad de letras es: "), (contador_letras(palabra)))