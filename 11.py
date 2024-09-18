try:
    a = int(input("Введите трехзначное число: "))
    if 100<a<1000:
        sum = int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2])
        umn = int(str(a)[0]) * int(str(a)[1]) * int(str(a)[2])
        print("сумма:", sum)
        print("произведение:", umn)
    else:
        print("вы ввели не трехзначное число")
except ValueError:
    print("Ввод только чисел")
finally:
    print("РАБОТАЕТ")
    