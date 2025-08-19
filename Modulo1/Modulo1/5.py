# le pedimos al usuario que ingrese su edad
edad = int(input("Ingresa tu edad: "))

# Condicionales para clasificar por edad
if edad < 13:
    print("Eres un niño.")
elif edad >= 13 and edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres un adulto.")
