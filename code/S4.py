string=input()
print("Длина строки ", len(string))
print(string.lower())
k=0
for i in string:
    if i==["a","o","i","e","u"]:
        k+=1
print("Кол-во гласных", k)
nstring=string.replace("ugly", "beauty")
print(string.startswith("The"))
print(string.endswith("end"))