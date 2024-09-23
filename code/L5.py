for i in range(10):
    print('i=', i)
    if i==0:
        i+=2
    if i==1:
        continue
    if i==2 or i==3:
        print("i=2 или i=3")
    elif i in [4,5,6]:
        print("i=4 или i=5 или i=6")
    else:
        break