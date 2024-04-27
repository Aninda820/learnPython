class A:
    classvar1 = 'I mam a class variable in class A'
    def __init__(self):
        self.var1 = "I am inside class A's contructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar2 = 'I am inside class B'
  
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B's contructor"
        self.classvar1 = "Instance var in class B"

a = A()
b = B()

print(b.classvar1)
print(b.special)