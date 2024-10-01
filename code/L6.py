def main(**kwargs):
    for i,j in kwargs.items():
        print(f"{i} mean {mean(j)}")

def mean(data):
    return sum(data)/len (data)

if __name__ == '__main__':
    main(x=[1,2,3],y=[3,3,0])