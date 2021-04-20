def inputstudentdetails():
    global FullName
    global City
    global Country
    global Region
    global Email
    global MailingAddress
    global PhoneNumber
    global Quiz1Score
    global Quiz2Score
    global Quiz3Score
    global Test1Score
    global Test2Score
    global ZoomCalls
    global Assignments
    global IdNumber
    global Gender
    print("Student Details")
    print("------------------------------------------------")
    FName=input("First Name: ")
    LName=input("Enter Last Name: ")
    FullName= FName + ' ' + LName
    Gender= str.upper(input("Enter the Gender (M/F): "))
    IdNumber= input("Enter Id Number: ")
    print("------------------------------------------------")
    print()
    print("Mailing Address")
    print("------------------------------------------------")
    MailingAddress=input("Enter Mailing Address: ")
    City=input("Enter City: ")
    Country=input("Enter Country : ")
    Region=str.upper(input("Region NB: (For Africa Use 'A' and Other Regions Use '0'): "))
    Email= input("Enter Email Address: ")
    PhoneNumber= input("Enter Phone Number: ")
    print("------------------------------------------------")
    print()
    print("Scores For Quizs (OUT OF 100 Points)")
    print("------------------------------------------------")
    Quiz1Score=float(input("Enter Quiz 1 Score: "))

    if Quiz1Score < 0 or Quiz1Score> 100:
        print("The Score entered is incorrect.")
        choice=str.upper(input("Do wish to start all over again?:  Y/N "))
        if choice=="Y":
                Quiz1Score=float(input("Enter Quiz 1 Score: "))
        else:
         print("Process termitted prematurely")

    Quiz2Score=float(input("Enter Quiz 2 Score: "))
    if Quiz2Score < 0 or Quiz2Score> 100:
        print("The Score entered is incorrect.")
        choice=str.upper(input("Do wish to start all over again?:  Y/N "))
        if choice=="Y":
                Quiz2Score=float(input("Enter Quiz 2 Score: "))
        else:
         print("Process termitted prematurely")
    Quiz3Score=float(input("Enter Quiz 3 Score: "))
    if Quiz3Score < 0 or Quiz3Score> 100:
        print("The Score entered is incorrect.")
        choice=str.upper(input("Do wish to start all over again?:  Y/N "))
        if choice=="Y":
                Quiz3Score=float(input("Enter Quiz 3 Score: "))
        else:
         print("Process termitted prematurely")
    print()
    print("Scores For Tests (OUT OF 100 Points)")
    print("------------------------------------------------")
    Test1Score=float(input("Enter Test 1 Score (Advanced Python Test): "))
    if Test1Score < 0 or Test1Score> 100:
        print("The Score entered is incorrect.")
        choice=str.upper(input("Do wish to start all over again?:  Y/N "))
        if choice=="Y":
                Test1Score=float(input("Enter Test 1 Score (Advanced Python Test): "))
        else:
         print("Process termitted prematurely")
    Test2Score=float(input("Enter Test 2 Score: (Expert Python Test): "))
    if Test2Score < 0 or Test2Score> 100:
        print("The Score entered is incorrect.")
        choice=str.upper(input("Do wish to start all over again?:  Y/N "))
        if choice=="Y":
                Test2Score=float(input("Enter Test 2 Score (Advanced Python Test): "))
        else:
         print("Process termitted prematurely")
    print("------------------------------------------------")
    print()
    print("Homework Programming Assignments (0-10)")
    Assignments= float(input("Enter Programming Assignment Score: "))
    print("Zoom Calls Attended (Out of 3 Zoom Calls)")
    ZoomCalls= float(input("Enter Zoom Calls Attended: "))

def CalculationsAndAward():
    global AssignScore
    global AveScore
    global ZoomScore
    global awardStatus
    AveScore = (((Quiz1Score + Quiz2Score + Quiz3Score + Test1Score + Test2Score) / 500) * 100)
    ZoomScore = ((ZoomCalls / 3) * 9)
    AssignScore = ((Assignments / 10) * 10)
    if Gender=="F" and AveScore>= 76:
        if Region =="A":
            awardStatus = "Full Scholarship Awarded"
        else:
            awardStatus = "Partial Scholarship Awarded"
    elif Gender=="M" and AveScore>= 80:
        if Region == "A":
            awardStatus = "Full Scholarship Awarded"
        else:
            awardStatus = "Partial Scholarship Awarded"
    else:
            awardStatus = "SORRY YOU DID NOT QUALIFY FOR A SCHOLARSHIP"

def PrintReport():
    #Display Report
    print("STUDENT SCHOLARSHP AWARD REPORT")
    print("-----------------------------------------------------------------------------------------")
    print()
    print("Student Name: " + FullName)
    print("Id Number: " + IdNumber)
    print("Gender: " + Gender)
    print("Mailing Address: " + MailingAddress + "City: " + City + " Country: " + Country)
    print("Region: " + Region)
    print("Email Address: " + Email)
    print("Phone Number: " + PhoneNumber)
    print()
    print("SCORES FOR QUIZZES")
    print("-----------------------------------------------------------------------------------------")
    print(str.upper(("Quiz 1 Score: " + str(Quiz1Score) + "  Quiz 2 Score: " + str(Quiz2Score) + "  Quiz 3 Score: " + str(Quiz3Score))))
    print()
    print("SCORES FOR TESTS")
    print("-----------------------------------------------------------------------------------------")
    print("Test 1 Score (Advanced Python Test): " + str(Test1Score))
    print("Test 2 Score: (Expert Python Test): " + str(Test2Score))
    print("-----------------------------------------------------------------------------------------")
    print()

    print("Assignments: " + str(AssignScore))
    print("Zoom Calls Attended: " + str(ZoomScore))

    print("Average Score: " + str(AveScore))
    print("AWARD STATUS: " + awardStatus)

numStudents= int(input("How many students do you want to add?: "))
i=1
while i <=numStudents:
    #CallStudentDetails Function
    inputstudentdetails()
    #Do the Maths Here and Award
    CalculationsAndAward()
    #Print Report Here
    PrintReport()
