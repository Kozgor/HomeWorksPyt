from account_manager.usermode import Users

while True:
    alpha = input("Hello! Welcome to Original python user database!\nEnter 1 to add new user\nEnter 2 to login user\nEnter 3 to delete user\n")
    if alpha == "1":
        name = input("Enter your name:\n")
        lastname = input("Enter your lastname:\n")
        username = input("Enter your username:\n")
        email = input("Enter your email:\n")
        password = input("Enter your password:\n")
        user = Users(name, lastname, username, email, password)
        user.save_user()
        break
    elif alpha == "2":
        username = input("Enter your username:\n")
        password = input("Enter your password:\n")
        user = Users('name', 'lastname', username, 'email', password)
        user.check_user()
        break
    elif alpha == "3":
        username = input("Enter your username to continue deleting:\n")
        user = Users('name', 'lastname', username, 'email', 'password')
        user.delete_user()
        break
    else: print("Try again")