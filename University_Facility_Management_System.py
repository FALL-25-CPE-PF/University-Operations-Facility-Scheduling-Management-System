<<<<<<< HEAD
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
=======
class Facility:
    def _init_(self):
        self.fid = None
        self.name = None
        self.capacity = None
        self.days = []
        self.slots = []
        self.status = "Active"
    def add_facility(self):
        self.fid = input("Enter facility ID: ")
        self.name = input("Enter facility name: ")
        self.capacity = int(input("Enter capacity: "))

        days_input = input("Enter available days (Mon,Tue,Wed): ")
        self.days = days_input.split(",")

        slots_input = input("Enter time slots (9-11,11-1): ")
        self.slots = slots_input.split(",")

        self.status = "Active"

        file_exists = os.path.exists(FACILITY_FILE)

        with open(FACILITY_FILE, "a", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["fid", "name", "capacity", "days", "slots", "status"]
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "fid": self.fid,
                "name": self.name,
                "capacity": self.capacity,
                "days": "|".join(self.days),
                "slots": "|".join(self.slots),
                "status": self.status
            })

        print("Facility added successfully")
    def view_facilities(self):
        if not os.path.exists(FACILITY_FILE):
            print("No facilities found")
            return

        print("\n--- ALL FACILITIES ---")

        with open(FACILITY_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(
                    row["fid"],
                    row["name"],
                    "Capacity:", row["capacity"],
                    "Status:", row["status"]
                )
     #  UPDATE FACILITY STATUS 
    def update_status(self):
        fid = input("Enter facility ID to update status: ")
        new_status = input("Enter new status (Active/Inactive): ")

        rows = []
        updated = False

        with open(FACILITY_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["fid"] == fid:
                    row["status"] = new_status
                    updated = True
                rows.append(row)

        if not updated:
            print("Facility not found")
            return

        with open(FACILITY_FILE, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["fid", "name", "capacity", "days", "slots", "status"]
            )
            writer.writeheader()
            writer.writerows(rows)

        print("Facility status updated")
    # check availability 
    def is_available(self, day, slot):
        if not os.path.exists(FACILITY_FILE):
            return False

        with open(FACILITY_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if (
                    row["fid"] == self.fid
                    and row["status"] == "Active"
                    and day in row["days"].split("|")
                    and slot in row["slots"].split("|")
                ):
                    return True
        return False
    
class Admin(User):

    def _init_(self):
        super()._init_()   # username, password, role inherited 
     #  admin menu
    def admin_menu(self):
        while True:
            print("\n========== ADMIN MODE ==========")
            print("1. Add Facility")
            print("2. View Facilities")
            print("3. Update Facility Status")
            print("4. View All Requests")
            print("5. Manage Requests (Approve / Reject)")
            print("6. Generate Schedule")
            print("7. Logout")

            choice = input("Select option: ")

            if choice == "1":
                f = Facility()
                f.add_facility()

            elif choice == "2":
                f = Facility()
                f.view_facilities()

            elif choice == "3":
                f = Facility()
                f.update_status()

            elif choice == "4":
                self.view_requests()

            elif choice == "5":
                self.manage_requests()
            
            elif choice == "6":
                self.generate_schedule()

            elif choice == "7":
                print("Admin logged out")
                break

            else:
                print("Invalid option")
    def view_requests(self):
        if not os.path.exists(REQUEST_FILE):
            print("No requests submitted yet.")
            return

        print("\n------ ALL REQUESTS ------")

        with open(REQUEST_FILE, "r") as f:
            reader = csv.DictReader(f)
            empty = True
            for i, row in enumerate(reader, start=1):
                empty = False
                print(
                    f"{i}. User: {row['user']} "
                    f"| Role: {row['role']} "
                    f"| Facility: {row['facility']} "
                    f"| Day: {row['day']} "
                    f"| Slot: {row['slot']} "
                    f"| Status: {row['status']}"
                )

        if empty:
            print("Request file is empty.") 
    def manage_requests(self):
        if not os.path.exists(REQUEST_FILE):
            print("No requests to manage.")
            return

        rows = []

        with open(REQUEST_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        if not rows:
            print("No requests found.")
            return

        print("\n--- PENDING REQUESTS--- ")
        pending = []

        for i, row in enumerate(rows, start=1):
            if row["status"] == "Pending":
                pending.append(i)
                print(
                    f"{i}. {row['user']} ({row['role']}) "
                    f"| {row['facility']} | {row['day']} | {row['slot']}"
                )

        if not pending:
            print("No pending requests.")
            return

        try:
            choice = int(input("Select request number: "))
        except ValueError:
            print("Invalid input.")
            return

        if choice not in pending:
            print("Invalid selection.")
            return

        action = input("Approve or Reject (A/R): ").lower()

        if action == "a":
            rows[choice - 1]["status"] = "Approved"
            print("Request approved.")

        elif action == "r":
            rows[choice - 1]["status"] = "Rejected"
            print("Request rejected.")

        else:
            print("Invalid action.")
            return

        with open(REQUEST_FILE, "w", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["user","role","facility","day","slot","purpose","status"]
            )
            writer.writeheader()
            writer.writerows(rows) 
    def generate_schedule(self):
        if not os.path.exists(REQUEST_FILE):
            print("No requests file found.")
            return

        scheduled_any = False
        file_exists = os.path.exists(SCHEDULE_FILE)

        with open(REQUEST_FILE, "r") as rf, open(SCHEDULE_FILE, "a", newline="") as sf:
            req_reader = csv.DictReader(rf)
            sch_writer = csv.DictWriter(
                sf,
                fieldnames=["facility", "day", "slot", "user", "role"]
            )

            if not file_exists:
                sch_writer.writeheader()

            for row in req_reader:
                if row["status"] == "Approved":
                    sch_writer.writerow({
                        "facility": row["facility"],
                        "day": row["day"],
                        "slot": row["slot"],
                        "user": row["user"],
                        "role": row["role"]
                    })
                    scheduled_any = True

        if scheduled_any:
            print("Schedule generated successfully.")
        else:
            print("No approved requests found.")
                  
        
           
     
>>>>>>> sairah
