Name=input("Please enter your name:")
Surname=input("Please enter your surname:")
Age=int(input("Please enter your age:"))
DOB=int(input("Please enter your date of birth(just year):"))

info=[Name, Surname, Age, DOB]

for i in info:
    print(i)
    
if Age<18:
    print("You cannot go out because it's too dangerous.")
else:
    print("You can go out to the street.")