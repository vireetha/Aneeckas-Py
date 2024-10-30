medical_Cause =input("did you have a medical cause Y or N : ")
attendance =  int(input("Enter the attendence of the student: "))
if medical_Cause == 'Y':
    print("You are allows")
else:
    if attendance >= 75:
        print("Allowed")
    else:
        print("Not allowed")
    