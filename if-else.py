a = 5
b = 7
if a == b:
    print("a равно b")
else:
    print("a НЕ равно b")

print("---------")

cost = 2000
if cost < 1000:
    print("Скидки нет")
elif cost < 3000:
    print("Скидка 5%")
elif cost < 5000:
    print("Скидка 7%")
else:
    print("Скидка 10%")

# практика 1
a = int(input("Введите целое число: "))
if a > 5:
    print("Введёное число больше 5")

# практика 2
a = int(input("Введите целое число: "))
if a >= 0:
    print(a+1)
else:
    print(a-2)