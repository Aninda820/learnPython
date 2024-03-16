class Dad:
    basketBall = 1

class Son(Dad):
    dance = 1
    basketBall = 8
    def is_dance(self):
        return f"Yes I dance {self.dance} no of time"

class GrandSon(Son):
    dance = 6
    def is_dance(self):
        return f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = GrandSon()

print(harry.is_dance())
print(harry.basketBall)