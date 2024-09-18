try:
    с = input("Введите Ваше имя:")
    a = int(input("Введите Ваш возраст:"))
    b = int(input("Введите Ваш Вес:"))
    d = float(input("Введите Ваш рост в метрах:"))
# формула индекса массы тела
    result = int(b)/float(d)**2 #вес делится на рост в квадрате
except (ValueError, TypeError):
    print("ПОЖАЛУЙСТА ВВОДИТЕ ТОЛЬКО ЧИСЛА")
else:
    print("Ваш лишний вес:", result)
finally:
    print("Вы готовы начать корректировку веса")
