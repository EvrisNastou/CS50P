str=input("Greeting: ")
str=str.lower()

if str.find("hello")!=-1:
    print("$0")
elif  str[0]=="h":
    print("$20")
else: print("$100")
