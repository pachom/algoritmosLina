# algoritmo que necesita obtener el promedio de
#un estudiante a partir de sus tres notas parciales.

x = input("Digite primera nota: ")
y = input("Digite segunda nota: ")
z = input("Digite tercera nota: ")

cantidadNotas = 3

promedio = (float(x) + float(y) + float(z))/cantidadNotas

print("el promedio de las notas", x, y, z," es: ", round(promedio,1))