from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce((lambda x, y: x + y), numbers)
average = sum_of_numbers / len(numbers)
print(average)