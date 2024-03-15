class Employee:
    no_of_leaves = 8
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name {self.name} salary {self.salary} and role is {self.role}"


    @classmethod
    def change_leaves(cls, newLeaves):
        cls.no_of_leaves = newLeaves

    @staticmethod                       # static method
    def print_good(string):
        print(f"Hey {string} I am good")


ram = Employee("Ram", "40k", "GOD")
krishna = Employee("Krishna", "66k", "GOD")

ram.change_leaves(34)
print(ram.no_of_leaves)
print(Employee.no_of_leaves)

print(ram.print_details())
print(krishna.print_details())

ram.print_good("Aninda")
