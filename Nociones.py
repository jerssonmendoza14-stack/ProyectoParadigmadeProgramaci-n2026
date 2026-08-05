# Hola mundo
# print("Hola mundo")
# Ctrl+k+c = permite comentar una linea de codigo
# Ctrl+k+u = permite descomentar una linea de codigo

# Nombre y edad
# nombre="Jersson"
# edad=29
# print(f"Hola, bienvenido {nombre} al curso de paradigmas de programación!")

#Tipos de variables
#variable de tipo cadena
nombre="Jersson"
apellido="Mendoza"
# variable de tipo entero
edad=29
# variable de tipo flotante
estatura=1.70
saludo=(f"Hola, bienvenido {nombre} {apellido} al curso de paradigmas de programación!. Tienes {edad} años y mides {estatura} cm. ")
print(saludo)

# variables booleanas
es_estudiante=True
tiene_permiso=False

#variables de tipo listas
numeros=[1,2,3,4,5]
nombres=["Jersson", "Pedro", "Maria"]

#variables de tipo diccionario
datos={"nombre":"Jersson", "apellido":"Mendoza", "edad":29, "estatura":1.70}

#operadores aritmeticos
a=5
b=3
suma=a+b
resta=a-b
multiplicacion=a*b
division=a/b
print(f"La suma de {a} y {b} es: {suma}")
print(f"La resta de {a} y {b} es: {resta}")
print(f"La multiplicación de {a} y {b} es: {multiplicacion}")
print(f"La división de {a} y {b} es: {division}")

#modulo
modulo=a%b
print(f"El módulo de {a} y {b} es: {modulo}")

#potencia
potencia=a**b
print(f"La potencia de {a} elevado a {b} es: {potencia}")

#Para recibir datos del usuario se utiliza la función input()
nombre=input("¿Cual es su nombre? ")
edad=input("¿Cual es su edad? ")
estatura=input("¿Cual es su estatura? ")
print(f"Hola, {nombre}, veo que tienes {edad} años y mides {estatura} cm.")