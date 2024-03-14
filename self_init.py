class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printDetails(self):
        return f"The name is {self.name} salary {self.salary} and role is {self.role}"


harry = Employee("Harry", "50k", "Programmer")
rohan = Employee("Rohan", "70k", "Developer")

# harry.name = "Harry"
# harry.salary = "20k"
# harry.role = "Programmer"

# rohan.name = "Rohan"
# rohan.salary = "30k"
# rohan.role = "Developer"


print(harry.printDetails())
print(rohan.printDetails())
