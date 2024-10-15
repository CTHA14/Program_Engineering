input = input("Введите числа: ")

def countNumbers(input: str):
    countDictonary = dict()
    for char in list(input):
        if int(char) in countDictonary:
            countDictonary[int(char)] += 1
        else:
            countDictonary[int(char)] = 1

    dictSortedByValues = list(dict(sorted(countDictonary.items(), key=lambda item: item[1], reverse=True)).items())[:3]
    first_three_dict = dict(dictSortedByValues)
    return dict(sorted(first_three_dict.items(), key=lambda item: item[0]))

if len(input) > 15:
    print(countNumbers(input))
else:
    print("Вы ввели мало чисел")