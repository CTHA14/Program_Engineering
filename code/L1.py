request=int(input('Введите номер кабинета: '))

dictionary={
    101: {'key':1234,'access':True},
    102: {'key':1337,'access':True},
    103: {'key':2002,'access':True},
    104: {'key':3713,'access':False},
    None: {'key':None,'access':None},
}

response=dictionary.get(request)
if not response:
    response=dictionary[None]
key=response.get('key')
access=response.get('access')
print(key,access)