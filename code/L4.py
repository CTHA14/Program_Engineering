def main(x,*args):
    one=x
    two=sum(args)
    three=len(args)
    print(f"one={one}, two={two}, three={three}")
    return x+sum(args)/len(args)

if __name__ == '__main__':
    res=main(1,2,5,4,3,6,7,8,9,0)
    print(f"\nresult={res}")