str=input("Input: ")

txt=""
for i in str:
    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
        continue
    else: txt+=i

print(f"Output {txt}")
