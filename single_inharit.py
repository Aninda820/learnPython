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

    @staticmethod
    def print_good(string):
        print(f"Hi {string} how are you?")


class Programmer(Employee):
    def __init__(self, name, salary, role, language):
        self.name = name
        self.salary = salary
        self.role = role
        self.language = language

    def print_prog(self):
        return f"The programmer's name is {self.name} salary is {self.salary} and role is {self.role}, know language is {self.language}"



ram = Employee("Ram", "40k", "GOD")
krishna = Employee("Krishna", "66k", "GOD")

subham = Programmer("Subham", 444, "Programmer", ["c", "java"])
rohit = Programmer("Rohit", 653, "Programmer", ['python', "Ruby"])

print(rohit.print_prog())
print(rohit.print_details())
print(rohit.language)
