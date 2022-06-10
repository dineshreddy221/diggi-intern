
class MyHome:
    """ This is my hometown."""
    class_variable = 'New house'

    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def show(self):
        print("*" * 15)
        print("color : ", self.color)
        print("rooms : ", self.rooms)
        print("*" * 15)


home = MyHome("White", 3)  # instance creation.
print(home.class_variable)

home.show()  # to call a method we need to use paranthesis

print(home.__doc__)

# gives the class variable.
print(home.class_variable)

# gives the instance variables in a dictionry
print(home.__dict__)
