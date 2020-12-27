
num = 3
studentname = "Zeynep Simay KILINÇ"
while num > 0:

    name = input("Please enter your name and surname:")
    
    if name == studentname:
        print("You can continue.")
        break
    elif name != studentname:
        print("Wrong name.")
        num = num-1
        print("You have ", num, " try remain.")
        if num ==0:
            print("Please try again later. ")
course=[]           
coursenum=5
while coursenum>0:
    coursen=input("Please enter a course:")
    coursenum= coursenum-1
    course.append(coursen)
    if coursenum ==0:
        print("Courses names are:", course)
        

x=3
while x>0:
    choise= input("Please choose 3 or 5 courses.")
    ch=len(choise)
#     for i in ch:
#         if i>=3 and i<=5:
#             print("i")
#         elif i<3 and i>5 :
#             print("You cannot choose less than 3 or more than 5.")
                    
    if choise in course:
        print("You can continue.")
        grades= {"midterm":85, "final":35, "project":75}
    #midterm=int(input("MT"))
    #final=int(input("final"))
    #project=int(input("project"))
        total=grades["midterm"]*(3/10)+grades["final"]*(5/10)+grades["project"]*(2/10)

        if total >= 90:
            print("The student should get AA.")
        elif total<90 and total>=70:
            print("The student should get BB.")
        elif total<70 and total>=50:
            print("The student should get CC.")
        elif total<50 and total>=30:
            print("The student should get DD.")
        elif total<30:
            print("You failed in class.")
        break
    elif choise not in course:
        x = x-1
        print("Choose one of the above courses!")
        

        