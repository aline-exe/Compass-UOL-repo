def soma(string_num):
    num = [int(x) for x in string_num.split(',')] #converter em int, split(',') divide os num
    resultado = sum(num)
    return resultado

string_num = "1,3,4,6,10,76"
soma = soma(string_num)

print(soma)
