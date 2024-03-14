class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = "20k"
harry.role = "Programmer"

rohan.name = "Rohan"
rohan.salary = "30k"
rohan.role = "Developer"


print(harry.name, harry.salary, harry.role)
print(harry.no_of_leaves)

print(rohan.name, rohan.salary, rohan.role)
print(rohan.no_of_leaves)

print(Employee.no_of_leaves)

# Employee.no_of_leaves = 9
# print(Employee.no_of_leaves)

rohan.no_of_leaves = 9
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)



print(type(rohan.__dict__))
print(rohan.__dict__)

print(Employee.__dict__)