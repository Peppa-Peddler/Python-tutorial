# Sintaxis básica

# Declaración de variable: IDENTIFICADOR = VALOR
a = 10
nacimiento = "05 de Abril de 2018"
calle = "1050"

# Imprimir en consola

print("Hola") # "Hola"
print(nacimiento) # "05 de Abril de 2018"

print(a) # 10
print(str(a)) # "10"

print(calle) # "1050"
print(int(calle)) # 1050

# Operaciones

calle = int(calle) # 1050
a = str(a) # "10"

Nombre = "Jorge"
Apellido = "Miranda"
Nombre_completo = Nombre + Apellido

print( 20 / 3 ) # 6.66666666
print( 20 // 3 ) # 6
print( 30 * 6 ) # 180
print( 105 % 6 ) # 3
print( 10 - 5 ) # 5
print( 20 + 30 ) # 50

# Arrays o vectores
pecados = ["lujuria","ira","soberbia","envidia","avaricia","pereza","gula"]
miMatriz = [45, 56, 67, 90, 123, 134]

print(pecados[1]) #ira
print(miMatriz[5]) #134

print( miMatriz[0] + miMatriz[1] )

cantidad_de_pecados = len(pecados) # 7
matrizlongitud = len(miMatriz) # 6

print(cantidad_de_pecados) # 7
print(matrizlongitud) # 6
