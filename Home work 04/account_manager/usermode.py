if __name__ == 'main':
    Users

class Users:
    def __init__(self, first_name, last_name, username, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password

    def show_user_info(self):
        print('First name:', self.__first_name, '\nLast name:',
              self.__last_name, '\nUsername', self.__username, '\npassword: *******')

    def save_user(self):
        username = []
        useremail = []
        with open('db.txt') as username_list:
            for listline in username_list:
                if len(listline.strip())>0:
                    item = listline.strip()
                    items = item.split('#')
                    username.append(items[2])
                    useremail.append(items[3])
        if self.__username in username and self.__email in useremail:
            print("This username and email address already exist in my data base!\nIf you forgot your password please try to remember it ^^")            
        elif self.__username in username:
            print("Take another username please.")
        elif self.__email in useremail:
            print("Take another email address please.")
        
        else:     
            f = open('db.txt', 'a')
            f.write(self.__first_name + "#" + self.__last_name + '#' +
                    self.__username + '#' + self.__email + '#' + self.__password+'\n')
            f.close()

    def check_user(self):
        userpairlib = {}
        with open('db.txt') as create_pair:
            for listline in create_pair:
                if len(listline.strip())>0:
                    item = listline.strip()
                    items = item.split('#')
                    userpairlib.update({items[2]:items[4]})
        condidtion = ''
        for key, value in userpairlib.items():
            if key == self.__username and value == self.__password:
                condidtion = "Succesfull login in!"
                break
            else: condidtion = "Wrong username or password!"
        print(condidtion)
        
    def delete_user(self):
        userpairlib = {}
        users = []
        n_users = []
        with open('db.txt') as create_pair:
            for listline in create_pair:
                if len(listline.strip())>0:
                    item = listline.strip()
                    items = item.split('#')
                    users.append(items)
                    n_users.append(items)
                    userpairlib.update({items[2]:items[4]})
        for key, value in userpairlib.items():
            truepass = value
        if key != self.__username:
            print("Wrong username!")
        elif key == self.__username:
            truepass = value
            trypass = input("Enter your password to continue deleting:\n")
            if trypass != truepass: print("Wrong password!")
            elif trypass == truepass:
                for index, list_of_users in enumerate(n_users):
                    if key == list_of_users[2]: 
                        del(n_users[index])
                        new_list = ''
                        for i in range(0, len(n_users)):
                            new_string = '#'.join(n_users[i])
                            new_string += '\n'
                            new_list += new_string
                        f = open('db.txt', 'w')
                        f.write(new_list)
                        f.close()
                        print("Your account was succesfully deleted!")