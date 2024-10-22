with open('input.txt','a+') as f:
    f.write('\nAdd line')

with open('input.txt','r') as f:
    result=f.readlines()
    print(result)