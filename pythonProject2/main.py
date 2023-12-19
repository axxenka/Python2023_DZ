exp = input("Введите выражение: ").split(' ')

fv = float(exp[0])
op = exp[1]
sv = float(exp[2])

if op == "+":
    print(fv + sv)
elif op == "-":
    print(fv - sv)
elif op == "*":
    print(fv * sv)
elif op == "/":
    print(fv / sv)


