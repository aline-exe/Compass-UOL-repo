a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

set_a = set(a)
set_b = set(b)

iguais = set_a.intersection(set_b)

print(list(iguais))
