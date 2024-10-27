#прямоугольный треугольник. пользователь вводит высоту
n = int(input("Введите высоту треугольника:  "))
for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    print()
