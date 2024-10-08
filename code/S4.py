a=[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
b=[]
for i in range(len(a)):
    if a[i]==3:
        a[i]=4
    if a[i]==2:
        b.append(i)
b.reverse()
for i in range(len(b)):
    a.pop(b[i])
print(a)