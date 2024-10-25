#Условия задач
#1. Вывести на экран столько элементов ряда Фибоначчи, сколько указал пользователь. Например, если на ввод поступило число 6,
# то вывод должен содержать шесть первых чисел ряда Фибоначчи: 1 2 3 5 8 13.
#2. Вычислить факториал введённого числа.

def fibonacci_sequence(n):
    a, b = 1, 2
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
n = int(input("Введите число: "))
print(" = Ряд Фибоначчи",(fibonacci_sequence(n)))
print("Факториал =", (factorial(n)))