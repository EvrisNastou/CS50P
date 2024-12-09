import validators

def main():
     print(check_validate(input("What's your email address? ")))

def check_validate(email):
    if validators.email(email) == True:
        return (f"Valid")
    else:
        return (f"Invalid")




if __name__=="__main__":
    main()
