lista = [
    "cachorro",
    "gato",
    "pombo",
    "rato",
    "pato",
    "porco",
    "lobo",
    "macaco",
    "raposa",
    "galinha",
    "galo",
    "urso",
    "coelho",
    "coruja",
    "zebra",
    "tigre",
    "jacaré",
    "elefante",
    "lagarto",
    "cobra",
]

lista.sort()

for animal in lista:
    print(animal)

with open("animais.csv", "w") as f:
    for animal in lista:
        f.write(animal + "\n")
