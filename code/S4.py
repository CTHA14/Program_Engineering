with open ('input1.txt','r', encoding='utf-8') as f:
    ifc=f.read()

with open('fwords.txt', 'r', encoding='utf-8') as fwords:
    fwl=fwords.read().split()

def find_substr(line, word):
    ind=[]
    t_line=line.lower()
    i=0
    while i<len(t_line):
        j=t_line.find(word,i)
        if j==-1:
            break
        ind.append(j)
        i=j+len(word)
    return ind

out_content=ifc

for word in fwl:
    ind=find_substr(out_content, word)

    for index in ind:
        out_content=(out_content[:index]+'*'*len(word)+out_content[index+len(word):])

print(out_content)