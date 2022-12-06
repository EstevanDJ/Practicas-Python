animales = ["gato", "perro"]
lista = []
for i in animales:
    for j in i:
        lista.extend(j)

print(lista)
