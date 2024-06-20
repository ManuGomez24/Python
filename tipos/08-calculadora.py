n1 = input("Ingresa el primer número: ")
n2 = input("Ingresa el segundo número: ")

try:
    n1 = int(n1)
    n2 = int(n2)
except ValueError:
    print("Por favor, ingresa números válidos.")
    exit(1)  # Salir del programa con un código de error

# Verificar la división por cero
if n2 == 0:
    print("No se puede dividir por cero.")
    exit(1)  # Salir del programa con un código de error

# Realizar las operaciones
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

# Crear el mensaje con los resultados
mensaje = f"""
Para los números {n1} y {n2}:
- El resultado de la suma es {suma}.
- El resultado de la resta es {resta}.
- El resultado de la multiplicación es {multi}.
- El resultado de la división es {div}.
"""

# Imprimir el mensaje
print(mensaje)
