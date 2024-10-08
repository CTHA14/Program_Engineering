def superset(set_1, set_2):
    if set_1>set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1==set_2:
        print('Множества равны')
    elif set_1<set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    else:
        print('Супермножества не обнаружено')

if __name__=='__main__':
    superset({1,8,3,6},{1,3})