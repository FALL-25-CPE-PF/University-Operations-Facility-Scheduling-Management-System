class Teacher(User):

    def _init_(self):
        super()._init_()
    def teacher_menu(self):
        while True:
            print("\n====== TEACHER MODE ======")
            print("1. Request Lecture / Lab")
            print("2. View My Requests")
            print("3. View My Schedule")
            print("4. Logout")

            choice = input("Select option: ")

            if choice == "1":
                self.request_facility()

            elif choice == "2":
                self.view_my_requests()

            elif choice == "3":
                self.view_my_schedule()

            elif choice == "4":
                print("Teacher logged out")
                break

            else:
                print("Invalid option")
    def request_facility(self):
        facility = input("Enter facility name: ")
        day = input("Enter day (Mon/Tue/Wed): ")
        slot = input("Enter time slot (9-11 / 11-1): ")
        purpose = input("Enter purpose (Lecture/Lab): ")

        file_exists = os.path.exists(REQUEST_FILE)

        with open(REQUEST_FILE, "a", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["user","role","facility","day","slot","purpose","status"]
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "user": self.username,
                "role": self.role,
                "facility": facility,
                "day": day,
                "slot": slot,
                "purpose": purpose,
                "status": "Pending"
            })

        print("Request submitted (Pending)")
    def view_my_requests(self):
        if not os.path.exists(REQUEST_FILE):
            print("No requests found.")
            return

        print("\n--- MY REQUESTS ---")

        with open(REQUEST_FILE, "r") as f:
            reader = csv.DictReader(f)
            found = False
            for row in reader:
                if row["user"] == self.username:
                    found = True
                    print(
                        "Facility:", row["facility"],
                        "| Day:", row["day"],
                        "| Slot:", row["slot"],
                        "| Status:", row["status"]
                    )

        if not found:
            print("No requests submitted yet.")
    def view_my_schedule(self):
        if not os.path.exists(SCHEDULE_FILE):
            print("No schedule available.")
            return

        print("\n--- MY SCHEDULE ---")

        with open(SCHEDULE_FILE, "r") as f:
            reader = csv.DictReader(f)
            found = False
            for row in reader:
                if row["user"] == self.username:
                    found = True
                    print(
                        "Facility:", row["facility"],
                        "| Day:", row["day"],
                        "| Slot:", row["slot"]
                    )

        if not found:
            print("No scheduled lectures yet.")
class Student(User):

    def _init_(self):
        super()._init_()   # username, password, role
    def student_menu(self):
        while True:
            print("\n====== STUDENT MODE ======")
            print("1. Request Facility")
            print("2. View My Requests")
            print("3. Cancel Pending Request")
            print("4. Logout")

            choice = input("Select option: ")

            if choice == "1":
                self.request_facility()

            elif choice == "2":
                self.view_my_requests()

            elif choice == "3":
                self.cancel_pending_request()

            elif choice == "4":
                print("Student logged out")
                break

            else:
                print("Invalid option")
    def request_facility(self):
        facility = input("Enter facility name: ")
        day = input("Enter day (Mon/Tue/Wed): ")
        slot = input("Enter time slot (9-11 / 11-1): ")
        purpose = input("Enter purpose (Practice/Event): ")

        file_exists = os.path.exists(REQUEST_FILE)

        with open(REQUEST_FILE, "a", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["user","role","facility","day","slot","purpose","status"]
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "user": self.username,
                "role": self.role,
                "facility": facility,
                "day": day,
                "slot": slot,
                "purpose": purpose,
                "status": "Pending"
            })

        print("Request submitted (Pending)")