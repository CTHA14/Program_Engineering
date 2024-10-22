from collections import Counter
x = open('input.txt', encoding='utf8').read()
c = Counter(x.split()) 
print(c.most_common()[:1])