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

# задача 7
# Найти периметр треугольника, заданного координатами своих вершин.
# (Определить функцию для расчета длины отрезка по координатам его  вершин.)
# def distance(x1, y1, x2, y2):
#     return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
#
# def triangle_perimetr(x1, y1, x2, y2, x3, y3):
#     a = distance(x1, y1, x2, y2)
#     b = distance(x2, y2, x3, y3)
#     c = distance(x3, y3, x1, y1)
#     return a + b + c
#
# print(triangle_perimetr(1, 2, 4, 5, 6, 7))


# задача 8
# Найти все трехзначные простые числа.
# (Определить функцию, позволяющую  распознавать простые числа.)

# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# primes = [i for i in range(100, 1000) if is_prime(i)]
# primes = []
# for i in range(100, 1000):
#     if is_prime(i):
#         primes.append(i)
# print(primes)

# Задача 9
# Получить все шестизначные счастливые номера.
# Счастливым называют такое  шестизначное число, в котором сумма
# его первых трёх цифр равна сумме его  последних трёх цифр.
# (Определить функцию для расчета суммы цифр  трёхзначного числа.)

# def sum_digits(n):
#     summa = 0
#     for d in str(n):
#         summa += int(d)
#     return summa
#
# def is_lucky(n):
#     s = str(n)
#     if sum_digits(s[:3]) == sum_digits(s[3:]):
#         print("Число счастливое")
#     else:
#         print("Число не счастливое")
#
# is_lucky(123456)

# Задача 10
# Даны шесть различных чисел.
# Определить максимальное из них.
# (Определить функцию, находящую максимум из двух различных чисел.)

# def max6(a, b, c, d, e, f):
#     return max(a, b, c, d, e, f)
#
# print(max6(2,4,5,6,89, 9))