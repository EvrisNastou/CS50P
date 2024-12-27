import sys
import csv
import pwinput
import os

def main():
    login()


def set_up(bankusers):
    try:
        with open(bankusers,"r") as file:
            database= csv.DictReader(file)
            return list(database)

    except FileNotFoundError:
            sys.exit(f"Could not read {bankusers}")


def renewal(bankusers, database):
    try:
        with open(bankusers,"w") as file:
            headers=["first" , "last", "username", "pin","money"]
            writer=csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(database)

    except FileNotFoundError:
        sys.exit(f"Could not read {bankusers}")


def editor(database,temp):
    i=0
    for row in database:
        if row['username']==temp['username']:
            break
        i+=1
    database[i]=temp

    return database


def login():
    database=set_up("bankusers.csv")
    while True:
        username=input("User Name: ")
        pin=pwinput.pwinput(prompt="Pin: ", mask="*")

        if username=="admin" and pin=="1111":
            renewal("bankusers.csv", database)
            break
        else:
            flag=False
            for i in database:
                if i['username']==username and i['pin']==pin:
                    flag=True
            if flag:
                menu(database,username)
            else:
                os.system("clear")
                print("Invalid name or pin")


def menu(database,username):
    os.system("clear")
    for row in database:
        if row['username']==username:
            break

    print(f"Welcome {row['first']} {row['last']}")

    while True:
        print("1 Account balance")
        print("2 Depostion")
        print("3 Withdrawl")
        print("4 Transfer")
        print("5 Sing out")
        choice=input("Choice: ")

        if choice=="1":
            os.system("clear")
            print(f"Your account amount is ${row['money']}")

        elif choice=="2":
            os.system("clear")
            dep=input("Enter the amount: ")
            row=deposition(row,dep)

        elif choice=="3":
            os.system("clear")
            withdr=input("Enter the amount: ")
            row=withdrawal(row,withdr)

        elif choice=="4":
            os.system("clear")
            user=input("Enter person's username: ")
            if correct_user(database, user):
                database,row=transfer(database,user,row)
                os.system("clear")
                print("The transfer end seccussful")

            else:
                print("Invalid username.")

        elif choice=="5":
            database=editor(database,row)
            os.system("clear")
            break

        else:
            os.system("clear")
            print("Invalid choice! Please try again")


def correct_user(database, user):
    flag=False
    for row in database:
        if row['username']==user:
            flag=True
    return flag


def deposition(personal_data,dep):
    try:
        if float(dep)<0:
            print("Invaid amount")

        else:
            new_amount=float(personal_data['money'])+float(dep)
            personal_data['money']=f"{new_amount:.2f}"
            print("Your deposition end successfully")

        return personal_data

    except ValueError:
        print("Invaid amount")
        return personal_data

def withdrawal(personal_data,withdr):
    try:
        if float(withdr)<0 or float(withdr)>float(personal_data['money']):
            print("Invaid amount")

        else:
            new_amount=float(personal_data['money'])-float(withdr)
            personal_data['money']=f"{new_amount:.2f}"
            print("Your withdrawal end successfully")

        return personal_data

    except ValueError:
        print("Invaid amount")
        return personal_data


def transfer(database,user,personal_data):
    i=0
    for temp in database:
        if temp['username']==user:
            break
        i+=1
    print(f"You transfer money to {temp['first']} {temp['last']}")
    amount=input("Enter the amount: ")
    try:
        if float(amount)>float(personal_data['money']) or float(amount)<0:
            print("Invalid value")
        else:

            database[i]['money']=f"{float(temp['money'])+float(amount):.2f}"
            personal_data['money']=f"{float(personal_data['money'])-float(amount):.2f}"

        return database,personal_data

    except ValueError:
        print("Invaid amount")
        return database, personal_data



if __name__ =="__main__":
    main()
