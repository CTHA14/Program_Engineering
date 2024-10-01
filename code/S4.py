def main(*args):
    a=sum(args)
    b=len(args)
    return sum(args)/len(args)

if __name__ == '__main__':
    res=main(1,2,5,4,3,6,7,8,9,10)
    print(f"result={res}")