# "1 2 3 4 5" найдите самое большое и маленькое число в этой строке и верните их кортежем

numbers = input("Введите числа: ")
array_numbers = numbers.split()
array_numbers = list(map(int, array_numbers))

min_max = min(array_numbers), max(array_numbers)
print(min_max)



