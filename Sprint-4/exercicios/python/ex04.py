def calcular_valor_maximo(operadores, operandos) -> float:
    valores = zip(operadores, operandos)
    resultados = map(lambda op: eval(f"{op[1][0]} {op[0]} {op[1][1]}"), valores)
    return max(resultados)


operadores = ["+", "-", "*", "/", "+"]
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]
rmaximo = calcular_valor_maximo(operadores, operandos)
print(rmaximo)
