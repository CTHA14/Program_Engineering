from math import sqrt
def geron(a,b,c):
    p=(a+b+c)/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s