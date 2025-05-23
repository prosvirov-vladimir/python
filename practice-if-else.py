# Задание 1
# Напишите программу, которая принимает на вход число от 1 до 7 и выводит соответствующий
# день недели (например, 1 - понедельник, 2 - вторник и т.д.).

# n = int(input("Введите число от 1 до 7: "))
# days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# if 1 <= n <= 7:
#     print(days[n - 1])
# else:
#     print("Некорректное число")

# Задание 2
# Напишите программу, которая принимает на вход число и проверяет, является ли оно чётным.
# Если число чётное, программа должна вывести сообщение "Число является чётным", в противном
# случае - "Число не является чётным".

# n = int(input("Введите число: "))
# if n % 2 == 0:
#     print("Число чётное")
# else:
#     print("Число не является чётным")
    
# Задание 3
# Напишите программу, которая принимает на вход число и проверяет, является ли оно
# однозначным, двузначным или трёхзначным. Выведите соответствующее сообщение: "Число
# однозначное", "Число двузначное", "Число трёхзначное".

# n = abs(int(input("Введите число: ")))
# if n < 10:
#     print("Число однозначное")
# elif n < 100:
#     print("Число двухзначное")
# elif n < 1000:
#     print("Число трёхзначное")
# else:
#     print("Число вне диапазона")

# Задание 4
# Напишите программу, которая принимает на вход возраст человека и выводит сообщение: "Вам
# можно голосовать", если возраст больше или равен 18, и "Вам нельзя голосовать" в противном
# случае.

# age = int(input("Введите возраст: "))
# if age >= 18:
#     print("Вам можно голосовать")
# else:
#     print("Вам нельзя голосовать")

# Задание 5
# Напишите программу, которая принимает на вход три числа и выводит наибольшее из них.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# print("Наибольшее число:", max(a, b, c))

# Задание 6
# Напишите программу, которая принимает на вход три числа и выводит сообщение "Среди чисел
# есть одинаковые", если хотя бы два числа равны между собой, и "Все числа различны" в
# противном случае.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# if a == b or b == c or a == c:
#     print("Среди чисел есть одинаковые")
# else:
#     print("Все числа различны")

# Задание 7
# Напишите программу, которая принимает на вход три числа и выводит их в порядке возрастания
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# nums = [a, b, c]
# nums.sort()
# print("Числа в порядке возрастания:", nums[0], nums[1], nums[2])

# Задание 8
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000
# — 5%, свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех
# менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

# sales1 = float(input("Введите уровень продаж первого менеджера: "))
# sales2 = float(input("Введите уровень продаж второго менеджера: "))
# sales3 = float(input("Введите уровень продаж третьего менеджера: "))
#
# # Расчёт ЗП первого менеджера
# if sales1 <= 500:
#     salary1 = 200 + sales1 * 0.03
# elif sales1 <= 1000:
#     salary1 = 200 + sales1 * 0.05
# else:
#     salary1 = 200 + sales1 * 0.08
#
# # Расчёт ЗП второго менеджера
# if sales2 <= 500:
#     salary2 = 200 + sales2 * 0.03
# elif sales2 <= 1000:
#     salary2 = 200 + sales2 * 0.05
# else:
#     salary2 = 200 + sales2 * 0.08
#
# # Расчёт ЗП третьего менеджера
# if sales3 <= 500:
#     salary3 = 200 + sales3 * 0.03
# elif sales3 <= 1000:
#     salary3 = 200 + sales3 * 0.05
# else:
#     salary3 = 200 + sales3 * 0.08
#
# # Определяем лучшего менеджера
# best_salary = max(salary1, salary2, salary3)
#
# if best_salary == salary1:
#     salary1 += 200
#     best = 1
# elif best_salary == salary2:
#     salary2 += 200
#     best = 2
# else:
#     salary3 += 200
#     best = 3
#
# print(f"Зарплата 1 менеджера: {salary1}")
# print(f"Зарплата 2 менеджера: {salary2}")
# print(f"Зарплата 3 менеджера: {salary3}")
# print(f"Лучший менеджер: {best}-ый")

# Задание 9
# Напишите программу, которая принимает на вход год и месяц, а затем выводит количество дней в
# этом месяце.
# year = int(input("Введите год: "))
# month = int(input("Введите номер месяца (1-12): "))
# if month == 2:
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("29 дней")
#     else:
#         print("28 дней")
# elif month in [1, 3, 5, 7, 8, 10, 12]:
#     print("31 день")
# elif month in [4, 6, 9, 11]:
#     print("30 дней")
# else:
#     print("Некорректный номер месяца")

# Задание 10
# Напишите программу для расчета стоимости билетов в кино в зависимости от возраста посетителя
# и времени сеанса. Условия следующие:
# Дети до 3 лет могут посещать кино бесплатно.
# Дети от 3 до 12 лет (включительно) платят 10$ за билет.
# Взрослые (старше 12 лет) платят 15$ за билет.
# Сеансы до 12:00 часов (включительно) имеют скидку 20% на стоимость билета.
# В остальное время сеансы не имеют скидки.
# Программа должна запрашивать у пользователя возраст и время сеанса, а затем выводить
# стоимость билета.

# age = int(input("Введите возраст: "))
# time = int(input("Введите время сеанса (в часах, например 14): "))
# price = 0
#
# if age < 3:
#     price = 0
# elif age <= 12:
#     price = 10
# else:
#     price = 15
#
# if time <= 12 and price > 0:
#     price *= 0.8
#
# print(f"Стоимость билета к оплате: {price}")