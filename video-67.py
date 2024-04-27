class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
    def printDetails(self):
        return f'The name is {self.name}, salary is {self.salary} and role is {self.role}'

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves
    
    def __add__(self, other):
        return self.salary + other.salary
        # return self.name + other.name

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return self.printDetails()      # I call the printDetails function hear

emp1 = Employee('Michael', 30, 'Software Engineer')
emp2 = Employee('Rohan', 45, 'Web Developer')

print(emp1 + emp2)
print(emp1)         # prafre to print str first then repr,  until we not define the str and repr function
print(repr(emp1))
print(str(emp1))