class Dec:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Function {self.func.__name__} is working")
        result = self.func(*args, **kwargs)
        print(f"Function {self.func.__name__} stopped working")
        return result
@Dec
def quadrat(a):
    print(a*a)
@Dec
def count(b):
    i=0
    c=0
    while (i<=b):
        c=i+c
        i=i+1
    print(c)
quadrat(3)
count(5)