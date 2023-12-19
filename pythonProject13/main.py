list_numbers = [38675, 455, 8, 15, 456, 77, 23, 777, 7567845, 5454] #list(map(int, input()))
result_square = [s ** 2 for s in list_numbers]
result_del = [s % 11 for s in list_numbers]
result_even = [s for s in list_numbers if s % 2 == 0]
result_number_odd = list(map(lambda x: len(str(x)), list_numbers))
result_number_odd_i = [list_numbers[i] for i in result_number_odd] #list(len(s) for s in result_number_odd if len(s) % 3 == 0)
result_even_numbers_twice = [list_numbers * 2 if s % 2 == 0 for s in list_numbers]
result_even_numbers_twice_i = result_even_numbers_twice * 4

print(result_square)
print(result_del)
print(result_even)
print(result_number_odd)
print(result_number_odd_i)
print(result_even_numbers_twice_i)
