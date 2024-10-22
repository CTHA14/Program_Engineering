inp=input('Введите данные: ')
with open('expenses.txt','a+') as f:
    f.write('\n'+inp)

with open('expenses.txt','r') as f:
    result=f.readlines()
    print(result)