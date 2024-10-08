lst = [1, 1, 3, 3, 1]
index = 0
while index < len(lst):
    cnt = lst.count(lst[index])
    if cnt > 1:
        lst[index] = str(lst[index]) * cnt
    index += 1
print(set(lst))