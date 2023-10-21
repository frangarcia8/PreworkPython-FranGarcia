'''Crea una función que, dado un número, verifique si un número es positivo,
negativo o cero.'''

def verificar_signo(num):
  if num > 0:
    return "Positivo"
  elif num < 0:
    return "Negativo"
  else:
    return "Cero"

num = float(input("Ingresa un número: "))
print (("El número es:"),verificar_signo(num))
  
  
  