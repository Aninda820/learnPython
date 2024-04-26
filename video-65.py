# Static Method in Python 


class Main:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    def printDetails(self):
        return f"The name is {self.name} and number is {self.num}"

    @staticmethod
    def sum(a, b):
        return a + b

rohan = Main('Rohan', 820700)
print(rohan.printDetails())
print(rohan.sum(10, 20))
print(Main.sum(10, 20))
# We can call static method by (class) as well as (instance of the class)
