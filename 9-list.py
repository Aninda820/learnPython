name = ['itachi', 'madara', 'saskey', 'naruto', 'boruto', 'minato']
print(name)

print(name[0])
print(name[3])
print(name[2])
print(name[5])

numbers = [3, 6, 11, 48, 33, 23, 99, 32]
print(numbers)
print(numbers[1:4])
print(numbers[:-2])
print(numbers[-4: -2])
print(numbers[::2])
print(numbers[::-3])

print(len(numbers))

# numbers.append(77)
numbers.insert(3, 96)   # (index, argument)
numbers.remove(6)
numbers.sort()
numbers.pop(6)


numbers[0] = 110
print(numbers)
