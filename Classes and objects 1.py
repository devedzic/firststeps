class Student:
    def __init__(self, name = ''):
        self.name = name
        print("Student")

    def print_name(self):
        print(self.name)

class MITstudent(Student):
    def __init__(self, name = ''):
        super().__init__(name)
        print("MIT student")

    def print_name(self):
        # print(self.name, "MIT student")
        super().print_name()    # alternatively: Student.print_name(self)
        print("MIT student")

john = Student("John")
john.print_name()
print()
john = MITstudent("John")
print()
john.print_name()

'''
print()
print("No. ", end='')
print(3)
'''
