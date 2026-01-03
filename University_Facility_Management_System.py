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