def check(tpl: tuple[int], id: int):
    try:
        first_idx = tpl.index(id)
    except ValueError:
        return ()     

    try:
        second_idx = tpl.index(id, first_idx + 1)
        return tpl[first_idx:second_idx + 1]
    except ValueError:
        return tpl[first_idx:]
    

test1 = (1, 2, 3)
test2 = (1, 8, 3, 4, 8, 8, 9, 2)
test3 = (1, 2, 8, 5, 1, 2, 9)

print(check(test1, 8))
print(check(test2, 8))
print(check(test3, 8))