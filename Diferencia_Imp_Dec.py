#Imperativa
numeros=[1, 2, 3, 4, 5]
cuadrados_pares=[]
for n in numeros:   
    if n%2==0:
        cuadrados_pares.append(n**2)
print(cuadrados_pares)

#Declarativa
numeros=[1, 2, 3, 4, 5]
cuadrados_pares=[n**2 for n in numeros if n%2==0]
print(cuadrados_pares)