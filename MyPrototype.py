class Student:
    def __init__(self, *, number, name):
        self.__number = number
        self.__name = name

    @property
    def number(self):
        return self.__number

    @property
    def name(self):
        return self.__name


student = Student(name='홍길동', number=10)

print(student)