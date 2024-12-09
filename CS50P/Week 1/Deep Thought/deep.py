str=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
str=str.lower()
str=str.strip()
if str=="42" or str=="forty-two" or str=="forty two" or str==" 42 ":
    print("Yes")
else: print("No")
