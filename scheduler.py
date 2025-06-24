exam = {
  "name": "",
  "date": "",
  "time": "",
  "room": "",
}

exam["name"] = input("Enter Name Exam: ")
exam["date"] = input("Enter Date: ")
exam["time"] = input("Enter Time: ")
exam["room"] = input("Enter Room: ")

exam.append({"name": exam, "date": exam, "time": exam, "room": exam})
print("Added Success")


# continue tomorrow