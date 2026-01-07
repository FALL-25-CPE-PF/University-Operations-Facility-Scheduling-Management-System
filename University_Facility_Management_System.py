import csv
import os

USERS_FILE = "users.csv"
FACILITY_FILE = "facilities.csv"
REQUEST_FILE = "requests.csv"
SCHEDULE_FILE = "schedule.csv"

class User:
    def _init_(self):
        self.username = None
        self.password = None
        self.role = None

    # ---------- REGISTER NEW USER ----------
    def register(self):
        username = input("Enter Username: ")
        file_exist = os.path.exists(USERS_FILE)
        
        if file_exist:
            with open(USERS_FILE, "r") as file:
                reader = csv.DictReader(file)
                for user in reader:
                    if username == user["username"]:
                        print("Username already exist!")
                        return
                    
        password = input("Enter Password: ")
        role = input("Enter role (admin/teacher/student): ").lower()
        user_found = False

        if not user_found:
            with open(USERS_FILE,"a",newline="") as file:
                writer = csv.DictWriter(file,fieldnames=["username","password","role"])
                if not file_exist:
                    writer.writeheader()
                writer.writerow({
                    "username": username,
                    "password": password,
                    "role": role
                    })
                print("Registered Successfully!")

    # ---------- LOGIN ----------
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not os.path.exists(USERS_FILE):
            print("No users found")
            return False

        with open(USERS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    self.username = username
                    self.password = password
                    self.role = row["role"]
                    print("Login successful")
                    return True

        print("Invalid username or password")
        return False
    
    # ---------- CHANGE PASSWORD ----------
    def change_password(self):
        try:
            with open(USERS_FILE,"r") as file:
                reader= csv.DictReader(file)
                users = []

                for record in reader:
                    if record:
                        users.append(record)

                found = False

                print("Please Verify your identity to continue.")
                username = input("Enter Username: ")
                for user in users:
                    if user["username"] == username:
                        old_password = input("Enter Old Password: ")
                        if user["password"] == old_password:
                            print("Verification Successfull!")
                            found = True
                            break
                        else:
                            print("Wrong Password!")
                        break
                else:
                    print("Wrong Username!")
                    
                if found:
                    with open(USERS_FILE, "w", newline="") as file:
                        writer = csv.DictWriter(file, fieldnames=["username","password","role"])
                        user["password"] = input("Enter new Password: ")
                        print("Password Changed Successfully!")
                        writer.writeheader()
                        for user in users:
                            writer.writerow(user)
        except FileNotFoundError:
            print("Record doesn't exist!")
    
    # ---------- VIEW PROFILE ----------
    def view_profile(self):
        print("\n--- USER PROFILE ---")
        print("Username:", self.username)
        print("Role:", self.role)
