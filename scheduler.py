examSchedule = []

while True:
    print("\nSmart Scheduler")
    print("1. Add New Exam")
    print("2. View All Exams")
    print("3. Edit Exam")
    print("4. Delete Exam")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        # ADD NEW EXAM
        name = input("Enter Name: ")
        date = input("Enter Date: ")
        time = input("Enter Time: ")
        room = input("Enter Room: ")

        exam = {
            "name": name,
            "date": date,
            "time": time,
            "room": room,
        }

        examSchedule.append(exam)

        print("Exam Add Successfully")

    elif choice == "2":
        # VIEW ALL EXAMS
        print("\nAll Exams:")
        if not examSchedule:
            print("No exams found.")
        else:
            for exam in examSchedule:
                print("Name:", exam["name"])
                print("Date:", exam["date"])
                print("Time:", exam["time"])
                print("Room:", exam["room"])

    elif choice == "3":
        # EDIT EXAM
        print("\nEdit Exam:")
        if not examSchedule:
            print("No exams to edit.")
        else:
            for index, exam in enumerate(examSchedule):
                print(f"{index}. {exam['name']} {exam['date']} {exam['time']} {exam['room']}")

            edit = int(input("Enter number you want to edit: "))

            name = input("Enter new Name: ")
            date = input("Enter new Date: ")
            time = input("Enter new Time: ")
            room = input("Enter new Room: ")

            exam = {
                "name": name,
                "date": date,
                "time": time,
                "room": room,
            }

            examSchedule[edit] = exam

            print("Exam Edit Successfully")

            # Show updated list
            print("\nUpdated Exam Schedule")
            for exam in examSchedule:
                print("Name:", exam["name"])
                print("Date:", exam["date"])
                print("Time:", exam["time"])
                print("Room:", exam["room"])

    elif choice == "4":
        # DELETE EXAM
        print("\nDelete Exam:")
        if not examSchedule:
            print("No exams to delete.")
        else:
            for index, exam in enumerate(examSchedule):
                print(f"{index}. {exam['name']} {exam['date']} {exam['time']} {exam['room']}")

            delete = int(input("Enter number you want to delete: "))
            examSchedule.pop(delete)

            print("Exam Deleted Successfully")

    elif choice == "5":
        print("Exiting Smart Scheduler. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")

# NEED TO DO IS EXPLAIN STEP BY STEP HOW PROCESS IS THIS THEN ITS DONE
# GREAT JOB MYSELF YOU DID IT!
# NOW YOU  CAN STUDY WEB DEV USING JAVASCRIPT