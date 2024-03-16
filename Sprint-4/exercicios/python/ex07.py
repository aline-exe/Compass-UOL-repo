def pares_ate(n: int):
    for i in range(2, n + 1, 2):
        yield i


n = 10
pares = pares_ate(n)

for valor in pares:
    print(valor)
