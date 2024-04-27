class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9     # This is protected variable
    __private = 98  # This is private variable

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name {self.name} salary {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves
    
    def from_desh(self, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print('This is good ' + string)


emp = Employee('Michael', 499, 'Programmer')
print(emp._protec)
print(emp._Employee__private)       # This is call name mangling