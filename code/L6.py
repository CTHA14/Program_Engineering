string = "We can not save you"
letter=input()
for i in string:
    if i==letter:
        print(f"letter '{letter}' is in the string")
        break
else:
    print(f"letter '{letter}' is not in the string")