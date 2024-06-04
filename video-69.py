# Class method in python  (setters and property Decorators)

class Employee:
    company = 'Apple'
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = 'Michael'
e1.show()
e1.changeCompany('Tesla')
e1.show()

print(Employee.company)
# class method help us to change the value directly from outside of the class instead of creating a new object and then changing it's values, this is called as "Class Method" in python because we can access any attribute or variable directly without creating an object first. This will be helpful if you want to create multiple objects with same attributes but different value for each oneof the 