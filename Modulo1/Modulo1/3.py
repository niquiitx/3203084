# Lista: se puede modificar
frutas = ["manzana", "banana", "pera"]
print("Lista de frutas:", frutas)
frutas.append("uva")  # Agrega un elemento
print("Frutas actualizadas:", frutas)

# Tupla: no se puede modificar 
colores = ("rojo", "verde", "azul")
print("Tupla de colores:", colores)

# Conjunto: no tiene orden y no repite elementos
numeros = {1, 2, 3, 2, 1}
print("Conjunto de números (sin duplicados):", numeros)

# Diccionario: clave-valor
persona = {
    "nombre": "Nicolás",
    "edad": 17,
    "ciudad": "Mosquera"
}
print("Diccionario de persona:", persona)
print("Nombre de la persona:", persona["nombre"])
