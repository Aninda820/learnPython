def cube(x):
    return x**3


# newList = []
l = [2, 3, 4, 5, 6]
# for item in l:
#     newList.append(cube(item))


# MAP
newList = list(map(cube, l))
# newList = list(map(lambda x: x**3, l))
print(newList)



# FILTER
def filter_function(a):
    return a>=4
newList1 = list(filter(filter_function, l))
print(newList1)



# REDUCE
from functools import reduce
def add(a, b):
    return a+b
sum = reduce(add, l)
print(sum)