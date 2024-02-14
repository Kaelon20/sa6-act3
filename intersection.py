list1 = [23, 65, 78, 34, 65, 26, 2, 7]
list2 = [60, 34, 26, 65, 22, 2, 43, 33]

intsect = list(filter(lambda x: x in list1, list2))
print(intsect)