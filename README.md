# Notebook
Este repositorio solamente contiene código brevemente comentado. Actualmente no pretende servir como tutorial propiamente, sino como cuaderno de anotaciones para clases que estoy dando. Aquí no se encontrarán explicaciones extensivas y detallas de lenguaje, pero si una breve guia para utilizar las diferentes funcionalidades que uno puede encontrarse y que ofrece python3.

## Empezar
La siguiente instruccion ejecuta python en la consola: `python [nombre del archivo]`

Ejemplo:
```
python basico.py
```
Notar que se debe usar la extensión `.py`.

Generalización: `python [ruta/del/archivo]`


## Instrucciones básicas
Los siguientes extractos pertenecen al archivo: [basico.py](basico.py)

```python
# Declaración de variable: [IDENTIFICADOR] = [VALOR]

a = 10
nacimiento = "05 de Abril de 2018"
calle = "1050"

```
En python se usa `#` para empezar un comentario.

La declaración de variables es de la forma  [IDENTIFICADOR] = [VALOR].
En este caso `a` se declara como un número entero de valor `10` y, `nacimiento` y `calle` como cadenas de caracteres (string) con los valores `"05 de Abril de 2018"` y `"1050"` respectivamente. Se usa `""` (doble comilla) para declarar una cadena de caracteres.

```python
# ...continuación del archivo

print("Hola") # "Hola"
print(nacimiento) # "05 de Abril de 2018"

print(a) # 10
print(str(a)) # "10"

print(calle) # "1050"
print(int(calle)) # 1050
```
la función `print` toma como argumento un valor y lo imprime en la consola.

En la instrucción `print(int(calle))` se hace llamado a la función `int` que retorna un entero en lugar del valor original (`"1050" -> 1050`), lo mismo sucede en `print(str(a))` con `str` que retorna un string en lugar del valor original (`10 -> "10"`).

```python
calle = int(calle) # 1050
a = str(a) # "10"

Nombre = "Jorge"
Apellido = "Miranda"

Nombre_completo = Nombre + " " + Apellido
# resultado: "Jorge Miranda", en python la suma en strings es una concatenación.

print( 20 / 3 ) # 6.66666666 <- División real
print( 20 // 3 ) # 6 <- División entera
print( 30 * 6 ) # 180 <- multiplicación
print( 105 % 6 ) # 3 <- módulo
print( 10 - 5 ) # 5 <- resta
print( 20 + 30 ) # 50 <- suma
```

### Arreglos o vectores
La indexación del arreglo empieza en `0`. Para acceder al `ì-esimo`(i>=0) valor se usa `nombre_array[i]`. Para obtener la cantidad de elementos se usa la función `len` (ej: ``len(miMatriz)`)

```python
pecados = ["lujuria","ira","soberbia","envidia","avaricia","pereza","gula"]
miMatriz = [45, 56, 67, 90, 123, 134]

print(pecados[1]) #ira
print(miMatriz[5]) #134

print( miMatriz[0] + miMatriz[1] )

cantidad_de_pecados = len(pecados) # 7
matrizlongitud = len(miMatriz) # 6

print(cantidad_de_pecados) # 7
print(matrizlongitud) # 6
```
