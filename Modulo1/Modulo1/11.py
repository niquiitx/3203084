# Definimos una clase llamada Persona
class Persona:
    # Método constructor: define qué tiene cada persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método que muestra un saludo
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creamos objetos (instancias) de la clase
persona1 = Persona("Nicolás", 17)
persona2 = Persona("Felipe", 20)

# Usamos métodos del objeto
persona1.saludar()
persona2.saludar()
