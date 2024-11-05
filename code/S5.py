class points:
    def calculation(self):
        pass

class rally(points):
    def calculation(self):
        print('1 - 30 points, 2 - 27 points, 3 - 25 points')

class F1(points):
    def calculation(self):
        print('1 - 25 points, 2 - 18 points, 3 - 15 points')

r=input()
if r==1:
    p_r=rally
    p_r.calculation()
elif r==2:
    p_f=F1
    p_f.calculation()