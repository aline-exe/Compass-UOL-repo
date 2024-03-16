class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade


valores = [
    ("BOIENG456", "1500 km/h", "400 passageiros"),
    ("Embraer Praetor 600", "863 km/h", "14 passageiros"),
    ("Antonov An-2", "258 km/h", "12 passageiros") ]

avioes = []

for valor in valores:
    modelo, velocidade, capacidade = valor
    aviao = Aviao(modelo, velocidade, capacidade)
    avioes.append(aviao)


for aviao in avioes:
    print(
        f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} e é da cor {aviao.cor}."
    )
