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
           
     