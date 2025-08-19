frutas = ["manzana", "pera"]

try:
    print(frutas[5])
except IndexError:
    print("Error: Ese índice no existe en la lista.")
