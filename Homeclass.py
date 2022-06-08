class MyHome:
  ''' This is my home town. '''
  class_variable = 'Red house'
  def display(self):   # self is mandatory in display the written content in this method
    print("Welcome to Anantapur successfull")

home = MyHome()     # instance creation.
print(home.class_variable)

home.display()  # to call a method we need to use paranthesis

print(home.__doc__)

# gives the class variable.
print(home.class_variable)

# gives the instance variables in a dictionry
print(home.__dict__)
