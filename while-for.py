# n = 5
# while n < 10:
#     n += 1
#     if n == 7:
#         continue
#     print(n)
#
# print("Цикл завершился")

# Задание 8
# Зарплата менеджера составляет 200$ + процент от продаж, продажи до 500$ — 3%, от 500 до 1000
# — 5%, свыше 1000 — 8%. Пользователь вводит с клавиатуры уровень продаж для трех
# менеджеров. Определить их зарплату, определить лучшего менеджера, начислить ему премию
# 200$, вывести итоги на экран.

# sales1 = float(input("Введите уровень продаж первого менеджера: "))
# sales2 = float(input("Введите уровень продаж второго менеджера: "))
# sales3 = float(input("Введите уровень продаж третьего менеджера: "))
#
# salaries = []
# for sales in [sales1, sales2, sales3]:
#     if sales <= 500:
#         percent = 0.03
#     elif sales <= 1000:
#         percent = 0.05
#     else:
#         percent = 0.08
#     salary = 200 + sales * percent
#     salaries.append(salary)
#
# # Определяем лучшего менеджера
# best_salary = max(salaries)
# best_index = salaries.index(best_salary)
# salaries[best_index] += 200
#
# print(f"Зарплата 1 менеджера: {salaries[0]}")
# print(f"Зарплата 2 менеджера: {salaries[1]}")
# print(f"Зарплата 3 менеджера: {salaries[2]}")
# print(f"Лучший менеджер: {best_index + 1}-ый")

# for x in range(5, 50, 5):
#     print(x)
#
# print("-------------")
#
# for x in range(50, 5, -5):
#     print(x)

# for x, y in enumerate(["Первый", "Второй", "Третий"]):
#     print(x, " - ", y)