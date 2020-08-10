# algoritmo que solicite un número entero 
# y muestre el nombre del mes correspondiente. 
# Ejemplo: Enero = 1.
# Lo idel sería utilizar un switch pero en python 
# no hay por lo que se simula con un diccionario

numeroMes = input("Digite un numero de mes menor o igual a 12: ")

def default():
   return "Opcion Invalida"

def switch(numero):
  sw = {
    1 : "Enero",
    2 : "Febrero",
    3 : "Marzo",
    4 : "Abril",
    5 : "Mayo",
    6 : "Junio",
    7 : "Julio",
    8 : "Agosto",
    9 : "Septiembre",
    10 : "Octubre",
    11 : "Noviembre",
    12 : "diciembre",
  }

  return sw.get(int(numeroMes), default())

nombreMes = switch(numeroMes)

print("el mes ", nombreMes," corresponde al: ", numeroMes)