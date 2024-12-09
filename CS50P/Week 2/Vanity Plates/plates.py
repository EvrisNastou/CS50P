def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:1].isalpha():
        if len(s)>=2 and len(s)<=6:
            i=0
            while i!=len(s)-1:
                if s[i].isdigit() and s[i+1].isalpha():
                    return False
                if s[i].isdigit()==False and s[i].isalpha()==False:
                    return False
                i+=1
            if s.find("0")!=-1:
                if s[s.find("0")-1].isalpha():
                    return False
            return True
        else: return False
    else: return False




main()
