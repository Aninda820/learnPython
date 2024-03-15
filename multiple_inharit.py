class Employee:
    no_of_leaves = 8
    var = 8
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


class Player:
    no_of_games = 4
    var = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The name is {self.name} Game is {self.game} and role is {self.role}"

class CoolProgrammer(Employee, Player):
    var = 10
    language = "Python"
    def print_language(self):
        return self.language
    pass




ram = Employee("Ram", "40k", "GOD")
krishna = Employee("Krishna", "66k", "GOD")

asok = Player("Asok", ["Cricket", "Volly"])
naruto = CoolProgrammer("Naruto", 4399, "Programmer")

det = naruto.print_details()
print(det)
print(naruto.print_language())

print(naruto.var)