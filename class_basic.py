# OOP - Object Oriented Programing
class Player:
    # Class Object Attribute
    membership = True

    def __init__(self, name, age):
        # Attributes
        self.name = name
        self.age = age

    def run(self):
        print(f'Run {self.name} Run!')
        return True


player1 = Player('Richard', 25)

print(player1)
print(player1.run())
print(player1.membership)  
