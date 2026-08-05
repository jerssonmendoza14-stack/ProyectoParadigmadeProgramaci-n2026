# nombre="Pedro"
# edad=29
# print("Hola, mi nombre es", nombre, "y tengo", edad, "años.")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1=Persona("Pedro", 29)
print(persona1.saludar())