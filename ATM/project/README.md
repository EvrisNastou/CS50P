# ATM
#### Video Demo: https://youtu.be/rWnKhjfc7yc
#### Description:

ATM is an application where you can deposit, withdrawal and transfer money from your account.

How does it work?  There is a csv file, where they admin can add customers with their personal information such as the first and last name, the username, the pin and their amount.  All this information are written in a matrix with dictionaries, because it is easier to search, compare and find the personal information of each user. Also, it is easier to renew the matrix than the file.
As a customer wants to make a transaction, she/he must enter her/his personal username and pin, which get hidden by the special character “*” so no one also can see her/his pin, in order to have access to her/his account. If they enter the wrong username or pin, the system won't allow them to sign in to their account and it will show them a message to try again. When customers enter to their account, a menu with 5 different options appears: 1. Account balance, 2. Deposition, 3 Withdrawal, 4. Transfer, 5. Sing out. Customers will be able to choose the option they want. If they enter an invalid input the system will show them the message “Invalid choice! Please try again” and they will have the possibility to choose again.  After any transaction, their amount will be renewed immediately. With option 1 the customer will be able to see their account balance. With option 2 the customer can deposit an amount in their personal account, but if the user gives a negative number or letters, the system will reject this input, it will print an error message and it will not change the amount. Option 3 gives the customer the possibility to take some money from his account. As in option 2, the system will check if the input is valid. As a result, the system is going to reject the input if it is a negative number, letters or if the input is bigger than the account balance.  Option 4 let the customers transfer money to another user of this bank. First, the user must enter the username of the person to whom she/he wants to transfer the money and if it exists, it will ask the user to enter the amount. Again, the system will check if the input is valid as option 3. Finally, option 5 signs out the user from his account and the system renews the main database. The administrator can close the application without a problem if he/she enters as username=admin and pin=1111. When the application is closed by the administrator the matrix is written to the file as a dictionary in order to renew the amounts and to be able to set a matrix with dictionaries when the application runs again.

**What does each function do?**

* **main()**: The main calls the *login()*.

* **login()**: This fuction calls the *set_up(bankusers)* to creat the database with the personal information. Also, tells to the user to enter her/his username and her/his pin and if they are correct it calls the *menu(database,username)* otherwise it prints *Invalid name or pin* and tells to the user to renter her/his personal information. If the admin gives as a username=admin and pin=1111 the ATM close successfully.

* **menu(database,username)**: It gives the user the option to choose and checks if user enters a valid input and give her/him the access to his option.

* **deposition(personal_data,dep)**: This fuction check if the amount is correct and add the amount to the balance.

* **withdrawal(personal_data,withdr)**: This fuction check if the amount is correct and subtract the amount fron the balance.

* **transfer(database,user,personal_data)**: This fuction ask from the user to enter the username of the person who want to transfer money and checks the amount.

* **correct_user(database, user)**: This fuction check if the username which be give by the customer is exist in the database and allows the transfer.

* **editor(database,temp)**: When a user sing out from his account, this function renew the matrix with dictionaries with the personal information of each user.

* **set_up(bankusers)**: Creats a matrix with dictionaries from the file *bankusers.csv* with the personal information of each user.

* **renewal(bankusers, database)**: Writes the matrix with dictionaries in the file *bankusers.csv* with the personal information of each user.


**Libraries**

* **os**: used to clear the terminal with the fuction *os.system("clear")*.

* **sys**: use of *sys.exit(error message)* to print an error and close the program safely.

* **csv**: use of *csv.DictReader(file)* and *open(bankusers,"r")* to write the csv as a dictionary and to open the file.

* **pwinput**: used to hide the pin with the fuction *pwinput.pwinput(prompt="Pin: ", mask="\*")*. You must do *pip install pwinput* before you run the project.
