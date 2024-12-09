str=input("camelCase: ")
txt=""
for i in str:
    if i.isupper():
        txt+="_"
        txt+=i.lower()
    else: txt+=i

print(txt)
