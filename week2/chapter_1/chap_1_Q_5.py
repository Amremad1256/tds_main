from functools import reduce
numbers = [1, 2, 3, 4, 5]
max_number = reduce((lambda x, y: x if x > y else y), numbers)
print(max_number)