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