import random

random_list = random.sample(range(500), 50)

# Ordenando a lista
random_list.sort()

mediana = 0
if len(random_list) % 2 == 0:
    meio1 = len(random_list) // 2
    meio2 = meio1 - 1
    mediana = (random_list[meio1] + random_list[meio2]) / 2
else: 
    meio = len(random_list) // 2
    mediana = random_list[meio]
    
media = sum(random_list) / len(random_list)

valor_minimo = min(random_list)

valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')


#(exemplo)Media: 279.46, Mediana: 286.5, Mínimo: 3, Máximo: 490