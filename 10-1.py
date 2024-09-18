try:
    print("Кто из Вас старше?")
    print("Введите дату рождения первого человека:")
    a1 = int(input("Год: "))
    b1 = int(input("Месяц: "))
    c1 = int(input("Число: "))
    print("Введите дату рождения второго человека:")
    a2 = int(input("Год: "))
    b2 = int(input("Месяц: "))
    c2 = int(input("Число: "))
    if a1 == a2:
        if b1 == b2:
            if c1 < c2:
                print("Первый старше")
            elif c1 == c2:
                print("Вы ровесники")
            else:
                print("Второй старше")
        elif b1 < b2:
            print("Первый старше")
        else:
            print("второй старше")
    elif a1 < a2:
        print("Первый страше")
    else:
        print("Второй старше")
finally:
    print("ПРОЕКТ ВЫПОЛНЕН")

