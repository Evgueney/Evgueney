a = int(input("Введите трезначное число: "))
if 100<a<1000:
    sum = int(str(a)[0]) + int(str(a)[1]) + int(str(a)[2])
    print(sum)
else:
    print("Число не трехзначное")
