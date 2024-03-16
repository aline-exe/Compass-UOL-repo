def my_map(lista, f):
    return [f(n) for n in lista]

def potencia(n):
    return n**2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = my_map(lista, potencia)
print (resultado)

