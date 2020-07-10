# algoritmo que solicite 2 numeros enteros y un operador
# aritmetico y luego debe de mostrar el resultado 
# de la operacion correspondiente.
# Lo idel sería utilizar un switch pero en python 
# no hay por lo que se simula con un diccionario

x = int(input("Digite un numero :"))
y = int(input("Digite otro numero :"))
operador = input("Digite el operador :")

def suma(a, b):
   return a + b

def resta(a, b):
   return a - b

def multiplicacion(a, b):
   return a * b

def division(a, b):
   return a / b

def default():
   return "Opcion Invalida"

def switch(operador, x, y):
  sw = {
    "+" : suma(x, y),
    "-" : resta(x, y),
    "*" : multiplicacion(x, y),
    "/" : division(x, y),
  }
  return sw.get(operador, default())

resultado = switch(operador, x, y)

print(x, operador, y, " = ", resultado)