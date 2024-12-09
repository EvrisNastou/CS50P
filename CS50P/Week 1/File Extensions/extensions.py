str=input("File name: ")
str=str.lower()

if str.find("gif")!=-1:
    txt="image/gif"
elif str.find("jpg")!=-1 or str.find("jpeg")!=-1:
    txt="image/jpeg"
elif str.find("png")!=-1:
    txt="image/png"
elif str.find("pdf")!=-1:
    txt="application/pdf"
elif str.find("txt")!=-1:
    txt="text/plain"
elif str.find("zip")!=-1:
    txt="application/zip"
else:txt="application/octet-stream"

print(txt)
