str=input("Expression: ")
list=str.split(" ")

if list[1]=="+":
    result=int(list[0])+int(list[2])
elif list[1]=="-":
    result=int(list[0])-int(list[2])
elif list[1]=="/":
    result=int(list[0])/int(list[2])
else: result=int(list[0])*int(list[2])

print(float(result))
