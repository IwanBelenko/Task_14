# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = int (input("Введите число: "))
a = 0
while (2**a<=n):
    print(f"{2**a}")
    a+=1
