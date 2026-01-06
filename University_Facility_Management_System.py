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
        
           
     
