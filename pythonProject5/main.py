a = int(input("start - "))
b = int(input("end - "))

if a >= b:
    a, b = b, a
print(a, b)

lst = []

while a <= b:
    lst.append(a)
    a += 1

lst_sum = 0
for i in lst:
    lst_sum += i


print("Cумма -", lst_sum)