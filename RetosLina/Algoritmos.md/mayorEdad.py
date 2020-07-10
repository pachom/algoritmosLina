# algoritmo que solicita la edad de dos personas
# y muestra en pantalla la edad del mayor.


edad1 = int(input("Digite edad de la primera persona :"))
edad2 = int(input("Digite edad de la segunda persona :"))



if edad1 < edad2 :
  edadMayor = edad2
else:
  edadMayor = edad1

print("El mayor de ", edad1, edad2," es ", edadMayor)