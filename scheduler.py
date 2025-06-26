examSchedule = [] #EMPTY LIST.   #THINKING PROPER VARIABLE NAME FOR EMPTY LIST

#USER TEXT INTERFACE
def userInterface():
    print("\nSmart Scheduler")
    print("1. Add New Exam")
    print("2. View All Exams")
    print("3. Edit Exam")
    print("4. Delete Exam")
    print("5. Exit")
    
def choiceFunction(choice, examSchedule):
    if choice == 1:
        addFunction(examSchedule)
    elif choice == 2:
        viewFunction(examSchedule)
    elif choice == 3:
        editFunction(examSchedule)
    elif choice == 4:
        deleteFunction(examSchedule)
    elif choice == 5:
        exitFunction()
    else:
        print("Invalid Choice. Please Enter 1-5.")

        #1. ADD NEW EXAM
def addFunction(examSchedule):
    name = input("Enter Name: ")
    date = input("Enter Date: ")
    time = input("Enter Time: ")
    room = input("Enter Room: ")

    examValue = {
        "name": name,
        "date": date,
        "time": time,
        "room": room,
    }

    examSchedule.append(examValue)
    print("Exam Added Successfully")
    
    #2. VIEW ALL EXAMS
def viewFunction(examSchedule):
    print("\nAll Exams:")
    if not examSchedule:
        print("No exams found.")
    else:
        for exam in examSchedule:
            print("Name:", exam["name"])
            print("Date:", exam["date"])
            print("Time:", exam["time"])
            print("Room:", exam["room"])

            #3. EDIT EXAM
def editFunction(examSchedule):
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

        examValue = {
            "name": name,
            "date": date,
            "time": time,
            "room": room,
        }

        examSchedule[edit] = examValue
        print("Exam Edited Successfully")

        #4. DELETE EXAM
def deleteFunction(examSchedule):
    print("\nDelete Exam:")
    if not examSchedule:
        print("No exams to delete.")
    else:
        for index, exam in enumerate(examSchedule):
            print(f"{index}. {exam['name']} {exam['date']} {exam['time']} {exam['room']}")

        delete = int(input("Enter number you want to delete: "))
        examSchedule.pop(delete)
        print("Exam Deleted Successfully")

        #5. EXIT
def exitFunction():
    print("Exit Successfully, Thank You!")
    exit()

#Main Program Loop
while True:
    userInterface()
    inputNumber = int(input("Enter Your Choice: "))
    choiceFunction(inputNumber, examSchedule)


 ##REFLECTION WHILE DOING THIS CRUD

## 1 My reflection while doing this code is when im creating it im struggling to how the store the data input user then show up them when they need to view it then edit.
## 2 Second i ecounter for input user when i input 2 they show the option but not efficient like i click 2 yes its 2 but in the data its as string not a integer so that time i want to solve the problem.
## 3 Maybe for the function cause each of them i need to create for the specific fucntion if user click 1 then show what 1 function it is.
## 4 I dont know if its okay to use twice dictionaries in different function like for edit and add.


#Optional: i want add function trim() if user accidentally click small latter its automatically capitalize first letter for better result.