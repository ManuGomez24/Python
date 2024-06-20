numeros = [2, 3, 5, 6, 6, 554, 2]


# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [["chanchito", 1],
            ["felipe", 5],
            ["pulga", 9],
            ]


usuarios.sort(key=lambda el: el[1])
print(usuarios)
