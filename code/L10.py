a=[1,3,4,5,7,9]
flag=False
for i in a:
    if i%2==0:
        flag=True
if flag is True:
    print("Есть четные числа")
else:
    print("Нет четных чисел")