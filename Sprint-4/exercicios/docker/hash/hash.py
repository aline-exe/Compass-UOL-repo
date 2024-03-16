import hashlib


while True:
    input_str = input("Digite uma palavra: ")
    hash = hashlib.sha1(input_str.encode()).hexdigest()
    nome_arquivo = f"{input_str}.txt"
    with open(nome_arquivo, "w") as file:
        file.write(f"{input_str}: {hash}\n")
        
    print(hash)

#usar -it