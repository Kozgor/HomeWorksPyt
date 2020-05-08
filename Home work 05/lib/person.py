import mysql.connector
if __name__ == "__main__":
    pass

class db_manager:

    def __init__(self, host, user, password):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pythonlogin")
        self.__cursor.execute("USE pythonlogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
    def menu(self):
        exit = False
        while not exit:
            choise = int(input("\n1. Regist new user\n2. LOGIN\n3. EDIT\n4. DELETE\n5. Show all users\n6. Search by username\n7. Search by email\n0. to exit\n=====> "))
            if choise == 0:
                exit = True
                print("      11111        1¶111¶¶¶\n    ¶1    1¶      ¶1      ¶¶\n   ¶¶      1¶    ¶¶        ¶\n   ¶        ¶1   ¶         ¶\n  1¶        ¶¶  ¶¶        1¶\n  1¶        ¶¶  ¶         ¶1\n  1¶        ¶¶  ¶        1¶\n  1¶        ¶1 ¶¶        ¶1\n  1¶        ¶  ¶¶       ¶¶\n   ¶        ¶  ¶        ¶\n   ¶       1¶ 1¶       ¶1\n   ¶1    11¶¶1¶¶11    ¶¶\n   ¶¶ 1¶11      11¶¶1 ¶\n   1¶¶1            1¶¶1\n   1¶                1¶1\n  1¶                   ¶\n  ¶                    ¶¶\n 1¶   1¶¶¶           1¶¶¶\n 1¶   ¶¶¶¶            ¶¶¶1\n 1¶    ¶¶1              ¶1\n  ¶1        1¶¶¶¶¶¶¶¶   ¶  __BYE-BYE!\n  1¶       ¶¶¶¶¶¶¶¶¶1  ¶1 /\n   1¶     ¶¶¶¶¶¶¶¶¶¶  ¶¶                  1¶¶¶¶¶¶\n    1¶¶    ¶¶¶¶¶¶¶¶1 ¶¶ 1               ¶¶¶¶¶¶¶¶¶¶\n      1¶¶1          11 11¶¶¶          1¶¶¶¶¶¶1\n      1111                 ¶¶¶     1¶¶¶¶¶1\n     ¶1                      ¶¶ 11¶¶¶¶¶\n    ¶¶                   ¶¶    ¶¶¶    ¶¶\n    ¶1         1¶¶¶¶1     ¶¶1¶¶¶¶¶    ¶1\n    ¶¶        ¶¶¶¶¶1      ¶¶¶¶¶¶111 1¶\n    ¶¶  1¶   ¶¶¶¶¶     1¶¶¶¶¶¶    11\n     ¶   ¶¶1¶¶¶¶¶¶1 1¶¶¶¶¶1  ¶¶\n     ¶1   ¶¶¶¶¶¶1¶¶¶¶¶¶¶1     ¶¶\n 1¶¶¶¶¶    ¶¶¶ 1¶¶¶¶¶¶         ¶¶\n¶¶¶¶¶¶¶¶    1¶\n¶¶¶¶            ¶¶\n¶¶¶¶¶¶¶¶1    ¶¶   ¶¶   1         ¶¶\n¶¶¶¶¶¶¶¶¶¶    ¶1   1¶¶¶¶¶         ¶1\n¶¶¶¶¶¶¶ ¶¶¶1  ¶   111¶¶1          1¶\n¶¶¶¶¶¶¶¶1¶¶111  ¶¶¶11              ¶¶\n ¶¶¶¶¶¶¶¶¶¶   1¶¶        1¶¶        1¶\n  ¶¶¶¶¶¶¶¶¶  1¶1      111  ¶1       ¶1\n   ¶¶¶¶¶¶¶¶1¶¶¶   1¶11     ¶¶      1¶\n    1¶¶¶¶¶¶¶¶      ¶¶      1¶1    1¶\n      1¶¶¶¶         ¶1       11111\n          ¶         1¶\n           ¶¶11111111")
            elif choise == 1:
                answer = self.__register()
                print(answer)
            elif choise == 2:
                answer = self.__login()
            elif choise == 3:
                answer = self.__edit()
            elif choise == 4:
                answer = self.__delete()
                print(answer)
            elif choise == 5:
                answer = self.__showallusers()
            elif choise == 6:
                answer = self.__searchname()
            elif choise == 7:
                answer = self.__searchemail()
            else: print("Try again")

    def __register(self):
        username = input("Enter username:\n")
        email = input("Enter email:\n")
        password = input("Enter password:\n")
        re_password = input("Confirm password:\n")

        if password != re_password:
            return "Password don't match"

        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            return "User exist"
        else: 
            sql = "INSERT INTO users (username, email, password) VALUES(%s, %s, %s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User was succesfully created!"
    
    def __login(self):
        username = input("Enter username:\n")
        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            password = input("Enter your password:\n")
            self.__cursor.execute("SELECT * FROM users WHERE password='" + password + "'")
            shallipass = self.__cursor.fetchone()
            if shallipass != None:
                print("Welcome,",username+"!","This is your unique privet room!")
            elif shallipass == None:
                print("YOU SHALL NOT PASS!")
        elif result == None: 
            print("Oops! User not found...")
    
    def __edit(self):
        username = input("Enter username:\n")
        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            edit_choise = int(input("1 - To change name\n2 - To change email\n3 - To change password\n===> "))
            if edit_choise == 1:
                new_username = input("Enter new username:\n===> ")
                sql = ("UPDATE `users` SET username = '"+new_username+"' WHERE username='" + username + "'")
            elif edit_choise == 2:
                new_useremail = input("Enter new email:\n===> ")
                sql = ("UPDATE `users` SET email = '"+new_useremail+"' WHERE username='" + username + "'")
            elif edit_choise == 3:
                validation = input("Please enter your old password:\n===> ")
                self.__cursor.execute("SELECT `username`, `password` FROM `users` WHERE password ='" + validation + "' AND username = '" + username + "'")
                serveranswer = self.__cursor.fetchone()
                if serveranswer!= None:
                    new_password = input("Enter new password:\n===> ")
                    conf_new_password = input("Confirm new password:\n===> ")
                    if new_password == conf_new_password:
                        sql = ("UPDATE `users` SET password = '"+new_password+"' WHERE username='" + username + "'")
                        self.__cursor.execute(sql)
                        self.__db.commit()
                        print(username + ", your data was succesfully updated!")
                    else: print(new_password , "has no match with" , conf_new_password + ". I'm sorry, but you should try again.")
                else: print("Your old password incorrect! Try again.")
            else: print("Wrong choice!")
        elif result == None:
            print("Wrong username!")

    def __delete(self):
        username = input("Enter username:\n")
        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            sql = "DELETE FROM users WHERE username = '" + username + "'"
        else: 
            return 'No match found'
        self.__cursor.execute(sql)
        self.__db.commit()
        print(username, "deleted")

    def __showallusers(self):
        admin = input("Enter admin name to get all database users:\n")
        if admin != 'admin':
            print("Please enter admin name first! Thank you.")
        elif admin == 'admin':
            self.__cursor.execute("SELECT * FROM users")
            result = self.__cursor.fetchall()
            print("\nUser list from the best database it the world:\n")
            for i in range(0, len(result)):
                print("Username:",result[i][1]+".", "User email:", result[i][2]+".", "User password:", result[i][3]+".")

    def __searchname(self):
        username = input("Enter username to get info\n===> ")
        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            print("User ID:", result[0], "\nUser name:", result[1], "\nUser email:", result[2],"\nUser password:", result[3])
        else: 
            return 'No match found'
        self.__db.commit()
        
    def __searchemail(self):
        usermail = input("Enter email to get info\n===> ")
        self.__cursor.execute("SELECT * FROM users WHERE email='" + usermail + "'")
        result = self.__cursor.fetchone()
        if result != None:
            print("User ID:", result[0], "\nUser name:", result[1], "\nUser email:", result[2],"\nUser password:", result[3])
        else: 
            return 'No match found'
        self.__db.commit()