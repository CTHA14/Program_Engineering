from random import randint

def cube(n):
    if n==5 or n==6:
        print(n)
        print("Вы победили")
    elif n==1 or n==2:
        print(n)
        print("Вы проиграли")
    else:
        print(n)
        cube(randint(1,6))

if __name__ == '__main__':
    cube(randint(1,6))