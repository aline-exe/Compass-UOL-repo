primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

for i, (primeiroNome, sobreNome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {primeiroNome} {sobreNome} está com {idade} anos")
