def primo(numero):
    if numero < 2:
        return False
    
    for i in range (2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

for numero in range(0, 101):
    if primo(numero):
        print(numero)
