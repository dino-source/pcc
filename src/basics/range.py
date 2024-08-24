lst = [1, 2, 3, 4]
print(lst)

lst = list(range(10, 21))
print(lst)

evens = list(range(10, 31, 2))
print(evens)

odds = list(range(11, 32, 2))
print(odds)

squares = [x**2 for x in range(1, 11)]
print(squares)

cubes = [x**3 for x in range(1, 11)]
print(cubes)

min_value_in_list_of_cubes = min(cubes)
print(min_value_in_list_of_cubes)

max_value_in_list_of_cubes = max(cubes)
print(max_value_in_list_of_cubes)

sum_of_digits_from_1_to_10 = sum(list(range(1, 11)))
print(sum_of_digits_from_1_to_10)
