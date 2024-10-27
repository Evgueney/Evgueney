#задачу на нахождение суммы цифр десятизначного числа
import random
n = random.randint(1000000000,9999999999)
print(n)
summ = 0
for i in str(n):
    summ+=int(i)
print(summ)