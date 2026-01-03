#Libraries 
import os
import csv

# Parent Class
class User:
    def __init__(self,name=None,id=None,role=None):
        self.name = name
        self.id = id
        self.role = role
    
    def register_user(self):
        field = ["username","password","role"]
        username = input("Enter Username: ")
        file_exist = os.path.exists("user_login.csv")
        
        if file_exist:
            with open("user_login.csv", "r") as file:
                reader = csv.DictReader(file)
                for user in reader:
                    if username == user["username"]:
                        print("Username already exist!")
                        return
                    
        password = input("Enter Password: ")
        role = input("Enter your Role: ").lower()
        user_found = False

        if not user_found:
            with open("user_login.csv","a",newline="") as file:
                writer = csv.DictWriter(file,fieldnames=field)
                if not file_exist:
                    writer.writeheader()
                writer.writerow({
                    "username": username,
                    "password": password,
                    "role": role
                    })
                print("Registered Successfully!")
    def login(self):
        try:
            username = input("Enter your Username: ")
            with open("user_login.csv", "r") as file:
                reader = csv.DictReader(file)
                for user in reader:
                    if username == user["username"]:
                        password = input("Enter your password: ")
                        if password == user["password"]:
                            print("Login Successfully!")
                            return
                    else:
                        print("Incorrect Username!")
                        break
                else:
                    print("Incorrect Details!")
        except FileNotFoundError:
            print("Record doesn't exist!")
    