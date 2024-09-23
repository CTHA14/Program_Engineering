i=int(input())
if 0<=i<=10:
    if i<4:
        print("Диапазон от 0 до 3")
    elif 3<i<7:
        print("Диапазон от 3 до 6")
    else:
        print("Диапазон от 6 до 10")
else:
    print("Вне диапазона")