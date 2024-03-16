import json

with open('person.json', 'r') as file:
    texto = json.load(file)

print(texto)
