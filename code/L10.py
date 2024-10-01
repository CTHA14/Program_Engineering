global result

def rectangle():
    a=float(input("Ширина: "))
    b=float(input("Высота: "))
    global result
    result = a*b

def triangle():
    a=float(input("Основание: "))
    h=float(input("Высота: "))
    global result
    result = a*h

figure=input()

if figure=="1":
    rectangle()
if figure=="2":
    triangle()
print (f"Площадь: {result}")