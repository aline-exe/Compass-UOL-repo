def maiores_que_media(conteudo:dict)->list:
    valores = list(conteudo.values())
    media = sum(valores) / len(valores)
    produtos_media = [
        (produto, preco) for produto, preco in conteudo.items() if preco > media
        ]
    produtos_media.sort(key=lambda x: x[1])
    return produtos_media

exemplo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

resultado = maiores_que_media(exemplo)
print(resultado)
