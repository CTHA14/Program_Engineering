class Error(Exception):
    pass
def check(value):
    if value <= 0:
        raise Error("Значение должно быть положительным!")
def process(value):
    try:
        check(value)
        print(f"Обработка значения: {value}")
    except Error as e:
        print(e)
process(0)
process(-5)
process(10)