
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
num = int(input("Введите целое число: "))
sum = 0
while (num != 0):
        sum = sum + num % 10
        num = num // 10
print("Сумма цифр числа равна: ", sum)

#с дробными не осилил






