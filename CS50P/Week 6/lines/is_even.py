#1nd block with comments
def main():
    n=input("Give a number: ")
    if is_even(n):
        print("Yes it is")
    else:
        print("No it isn't")

#2nd block with comments
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#3nd block with comments

if __name__=="__main__":
    main()
