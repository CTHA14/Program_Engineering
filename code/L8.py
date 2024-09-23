a=0
while a<100:
    if a==0:
        a+=10
    elif a//5>1:
        a*=5
    else:
        a-=5
    print(a)