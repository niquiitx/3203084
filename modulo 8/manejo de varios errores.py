try:
    x = int("10")
    y = 5 / 0
except ValueError:
    print("Error de conversión.")
except ZeroDivisionError:
    print("Error: División entre cero.")
