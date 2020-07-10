# algoritmo que lee 3 números enteros diferentes
# entre sí y determina el número mayor de los tres
# Lo idel sería utilizar un switch pero en python 
# no hay por lo que se simula con un diccionario

x = int(input("Digite primer numero :"))
y = int(input("Digite segundo numero :"))
z = int(input("Digite tercer numero :"))


if x < y :
  if y < z:
    mayor = z
  else:
    mayor = y
elif x < z:
  mayor = z
else:
  mayor = x

print("mayor de ", x, y, z, " = ", mayor)