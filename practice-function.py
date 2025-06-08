# def greeting():
#     name = input("Введите ваше имя: ")
#     print("-----")
#     print(f"Привет {name}, добро пожаловать!")
#     print("-----")
#
# greeting()

# def summa(a, b):
#     c = a + b
#     return c
#
# print(summa(2, 2))
#
# result = summa(5, 5) - summa(1, 1) - summa(3,3) * summa(2,6)
# print(result)

# def f(a):
#     global b
#     b += 3
#     print(a + b)
#
# b = 2
# f(b)

# задача 1
# def print_lines(n):
#     print("-" * n)
#     print("-" * n)
#
# n = int(input("Введите количество символов в строке: "))
# print_lines(n)

# задача 2
# def print_rectangle(n):
#     if n < 2:
#         print("Ширина должна не менее 2-х")
#     print("-" * n)
#     print("-" + " " * (n - 2) + "-")
#     print("-" * n)
#
# n = int(input("Введите ширину прямоугольника: "))
# print_rectangle(n)

# задача 3
# def print_triangle():
#     n = int(input("Введите сторону треугольника: "))
#     for i in range(1, n + 1):
#         print("*" * i)
#
# print_triangle()

