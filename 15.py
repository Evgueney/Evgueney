#Пользователь воодит число N, нужно вывести все простые число до N
#5,7,11,14,15,17
#5+1=5+1
a = int(input("Введите число "))
for i in range(1,a):
    summ = 0
    for j in range(1,i+1):
        if i%j == 0:
            summ+=j
        if i+1 == summ:
            print("число" + str(i) + " простое")

