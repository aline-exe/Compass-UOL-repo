class Calculo:
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
x = 4
y = 5

calculo = Calculo()

resultado_soma = calculo.soma(x, y)
print (f'Somando: {resultado_soma}')

resultado_subtracao = calculo.subtracao(x,y)
print (f'Subtraindo: {resultado_subtracao}')