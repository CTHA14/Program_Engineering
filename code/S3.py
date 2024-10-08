from math import sqrt
def geron(a,b,c):
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
one.sort()
two.sort()
three.sort()
a1=one[0]
a2=one[-1]
b1=two[0]
b2=two[-1]
c1=three[0]
c2=three[-1]
print(geron(a1,b1,c1))
print(geron(a2,b2,c2))