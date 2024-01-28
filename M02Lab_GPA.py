##Suzette Irizarry
##M02Lab_GPA
###This app is meant to accept a student's GPA and determine whether the student has entered the Dean's List or Honor Roll 

DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25

while True:
    last_name: str = input("Enter student's last name [ZZZ to quit]:")
    if last_name.upper() == "ZZZ":
        break
    
    if last_name == str():
        continue
    
    first_name: str = input("Enter student's first name:")
    gpa: float = float(input("Enter student's GPA:"))
    
    if gpa >= DEANS_LIST:
        print("You have made it to the Dean's List!")
    elif gpa >= HONOR_ROLL:
        print("You have made Honor Roll!")
    else:
        break
         
    
    
    