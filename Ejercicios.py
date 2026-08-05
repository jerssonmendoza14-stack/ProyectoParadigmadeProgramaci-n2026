# El programa debe iniciar con un saldo disponible de $100.000. Posteriormente, deberá solicitar al usuario el valor que desea retirar y verificar si el monto solicitado es menor o igual al saldo disponible.
#imperativa
# saldo=100000
# retiro=int(input("Ingrese el valor que desea retirar: "))
# if retiro <= saldo:
#     saldo -= retiro
#     print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")

# #declarativa
# saldo=100000
# retiro=int(input("Ingrese el valor que desea retirar: "))
# nuevo_saldo = saldo - retiro if retiro <= saldo else saldo
# print(f"Retiro exitoso. Su nuevo saldo es: ${nuevo_saldo}")

#Ejercicio en casa
nombre=input("Ingrese su nombre: ")
horas_trabajadas=float(input("Ingrese el número de horas trabajadas: "))
valor_hora=float(input("Ingrese el valor por hora trabajada: "))
salario=horas_trabajadas*valor_hora
if salario > 2000000:
    salario -= salario*0.10
    print(f"Hola {nombre}, su nuevo salario después de aplicar un descuento del 10% por superar los $2.000.000 es: ${salario}")
else:
    print(f"Hola {nombre}, su salario es: ${salario}")
