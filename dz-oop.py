# Задание 1:
# Создайте класс Rectangle, который будет содержать атрибуты width и height
# и методы area() и perimeter().
#
# Создайте класс Square, который будет наследовать класс Rectangle и содержать
# только атрибут side (а не width и height).

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimetr(self):
#         return 2 * (self.width + self.height)
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#         self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def perimetr(self):
#         return 4 * self.side
#
# rect = Rectangle(4, 5)
# print("Площадь прямоугольника:", rect.area())
# print("Периметр прямоугольника:", rect.perimetr())
#
# sq = Square(3)
# print("Площадь квадрата:", sq.area())
# print("Периметр квадрата:", sq.perimetr())

# Задание 2:
# Создайте класс Person, который будет содержать атрибуты name, age, gender
# и метод introduce(), который будет выводить на экран информацию о человеке.
#
# Создайте класс Employee, который будет наследовать класс Person и содержать
# атрибуты salary и position, а также метод work(), который будет выводить на экран
# информацию о работе сотрудника.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")

class Employee(Person):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

    def work(self):
        print(f"{self.name} работает в качестве {self.position} с ЗП {self.salary} рублей.")


person = Person("Алиса", 30, "женский")
person.introduce()

employee = Employee("Алексей", 28, "мужской", "200 тыс.", "QA Senior")
employee.introduce()
employee.work()