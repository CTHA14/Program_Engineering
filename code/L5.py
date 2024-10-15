def tuple_sort(tpl):
    for e in tpl:
        if not isinstance(e,int):
            return tpl
    return tuple(sorted(tpl))

if __name__=='__main__':
    print(tuple_sort((5,5,5,6,3,2)))
    print(tuple_sort((5,5,5,6,'3',2)))