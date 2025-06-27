examSchedule = []

# USER TEXT INTERFACE
## USING THIS USER CAN CHOICE WHAT NUMBER THEY WANT TO SPECIFIC FUNCTION
def userInterface():
    print("\nSmart Scheduler")
    print("1. Add New Exam")
    print("2. View All Exams")
    print("3. Edit Exam")
    print("4. Delete Exam")
    print("5. Exit")
    
# USING THIS CONDITIONAL STATEMENT IF USER PRESS ANY NUMBER HAVE FUNCTION. THEN USER GOTO THE SPECIFIC FUNCTION
## I CREATE 1 - 5 FUNCTIONS THEN EVERY EACH OF THEM HAVE EQUIVALENT FUNCTION
### THEN IF USER PRESS NONE OF THE OPTIONS THEN ELSE CONDITION SHOW UP FOR INVALID USER CHOICE
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

# 1. ADD NEW EXAM
## FOR THIS FUNCTION GET USER ADD INFORMATION THEN STORE IT INTO EXAMVALUE DICTIONARIE THEN STORE IT INTO LIST USING APPEND FUCNTION
### THEN AFTER THAT IF COMPLETELY DONE THE PRINT FUNCTION SHOW UP EXAM ADD SUCCESSFULLY
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
## THIS FUNCTION SHOW ALL VALUES INSIDE OF IT THEN I USED CONDITIONAL STATEMENT FOR THE CHECKING IF THE EXAM IS EMPTY THE PRINT FUNCTION SHOW UP NO EXAM FOUND
### ELSE IF HAVE VALUE INSIDE IT CODE RUN THEN FOOR LOOP IS WORKING CHECK THE ALL VALUE INSIDE OF IT THEN SHOW IT ALL
def viewFunction(examSchedule):
    print("\nAll Exams:")
    if not examSchedule:
        print("No Exams Found.")
    else:
        for examValue in examSchedule:
            print("Name:", examValue["name"])
            print("Date:", examValue["date"])
            print("Time:", examValue["time"])
            print("Room:", examValue["room"])

#3. EDIT EXAM
## THE FUNCTION FOR THIS I USED CONDITIONAL STATEMENT CHECK IF THE HAVE VALUE OR NOTHING IF EMPTY THE PRINT FUNCTION SHOW UP LIKE NO EXAMS TO EDIT
### THEN IF HAVE VALUE ELSE FUNCTION WORKING INSIDE THEM I USED FOR LOOP FOR CHECK ALL INDEX AND VALUES INSIDE OF THEM
#### AFTER THE USER PICK WHAT INDEX VALUE ITS STORE INTO EXAMVALUE DICTIONARIES THEN STORE IN INTO LIST IN EXAMSHEDULE
def editFunction(examSchedule):
    print("\nEdit Exam:")
    if not examSchedule:
        print("No Exams To Edit.")
    else:
        for index, examValue in enumerate(examSchedule):
            print(f"{index}. {examValue['name']} {examValue['date']} {examValue['time']} {examValue['room']}")

        edit = int(input("Enter Index Number You Want To Edit: "))
        name = input("Enter New Name: ")
        date = input("Enter New Date: ")
        time = input("Enter New Time: ")
        room = input("Enter New Room: ")

        examValue = {
            "name": name,
            "date": date,
            "time": time,
            "room": room,
        }

        examSchedule[edit] = examValue
        print("Exam Edited Successfully")

#4. DELETE EXAM
## SAME AS PREVIOUS I USED CONDITIONAL STATEMENT FOR CHECKING IF THE VALUE IS EMPTY OR NOT
### THEN IF HAVE VALUE I USED FORLOOP CHECK THE INDEX AND VALUE THEN WHAT USER WANT TO DELETE
#### I USED POP() FUNCTION TO DELETE THE VALUE
def deleteFunction(examSchedule):
    print("\nDelete Exam:")
    if not examSchedule:
        print("No Exams To Delete.")
    else:
        for index, examValue in enumerate(examSchedule):
            print(f"{index}. {examValue['name']} {examValue['date']} {examValue['time']} {examValue['room']}")

        delete = int(input("Enter Index Number You Want To Delete: "))
        examSchedule.pop(delete)
        print("Exam Deleted Successfully")

#5. EXIT PROGRAM
## IF USER PRES NUMBER 5 AUTOMATICALLY EXIT THE PROGRAM THEN PRINT FUNCTION SHOW UP EXIT SUCCESSFULLY, THANK YOU!
def exitFunction():
    print("Exit Successfully, Thank You!")
    exit()

 # WHILE TRUE FUNCTION FOR THE REPEATEDLY  SHOW  USER INTERFACE MENU
 ## EVERY USER DONE FOR EACH FUNCTION THE WHILE TRUE FUNCTION SHOW UP THEN USER CAN DECIDE WHAT NEXT TO DO
while True:
    userInterface()
    inputNumber = int(input("Enter Your Choice: "))
    choiceFunction(inputNumber, examSchedule)