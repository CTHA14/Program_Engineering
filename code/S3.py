def func(value):
    try:
        numb = int(value)
        return numb*numb 
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")
print(func("aaAAaa"))
print(func(33))