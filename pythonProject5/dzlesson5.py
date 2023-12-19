a = int(input("Введите число 1 - "))
b = int(input("Введите число 2 - "))

na = a
nb = b

while na != nb:
    if na > nb: na = na - nb
    else: nb = nb - na
nod = na
nok = a * b // nod

print("НОК", nok)