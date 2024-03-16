def ler_num(number_txt):
    with open(number_txt, "r") as txt:
        return [int(line.strip()) for line in txt]


number_txt = "Sprint-4\\exercicios\\python\\number.txt"

numeros = ler_num(number_txt)  # função ler_num

maiores_pares = sorted(filter(lambda x: x % 2 == 0, numeros), reverse=True)[
    :5
]  # filtrar os pares e ordenar em desc
maiores_pares = list(map(int, maiores_pares))  # usando map

soma = sum(maiores_pares)

print(maiores_pares)
print(soma)
