class Employee:
    no_of_leavs = 8

    def __init__ (self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        
    def printDetails(self):
        return f"The name {self.name} salary {self.salary} and role is {self.role}"



harry = Employee("Harry", 434, "HR")
rohan = Employee("Rohan", 433, "Employee")

# harry.name = "Harry"
# harry.salary = 445
# harry.role = "Devoloper"


# rohan.name = "Rohan"
# rohan.salary = 3334
# rohan.role = "HR"

print(harry.printDetails())
print(rohan.printDetails())