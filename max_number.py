from functools import reduce

numbers = [21, 46, 3, 87, 56, 78, 80]

max_number = reduce(lambda x, y: x if x > y else y, numbers )
print(max_number)