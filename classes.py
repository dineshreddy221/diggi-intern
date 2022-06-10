# creating a class
class Student:
    def __init__(self, p):
        self.price = p

    def show(self):
        print("price : ", self.price)


std = Student(35)
print(std.price)

std.show()


# inheritance
class Student:
    def m_1(self):
        print("class- Student, m_1")

    def m_2(self):
        print("class - Student, m_2")


class Teacher(Student):
    def m_3(self):
        print("class - teacher, m_3")

    def m_4(self):
        print("class - teacher, m_4")


a = Student()
b = Teacher()

# teacher class inherits the properties of Student class
b.m_1()
b.m_2()
b.m_3()
b.m_4()
