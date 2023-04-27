numOfgradesEntered = int(input("Please enter a number of grades you would like to enter professor!(2-5): "))
if numOfgradesEntered <= 1:
    print("Sorry that wouldnt be applicable here")
elif numOfgradesEntered > 5:
    print("Sorry that wouldnt be applicable here")


while numOfgradesEntered == 2:
    name = input("Please enter a students Name: ")
    if name == " ":
        print("No students name was entered!")

    
    
    grade1 = float(input("Please enter a grade for the students class work: "))
    grade2 = float(input("Please enter a grade for the students homework: "))


    sumOfallGrades = grade1+grade2
    average = sumOfallGrades/2

    print("The student " + name + " average is " + str(average))

    if average >= 90:
        print(name + "is passing with an letter grade of A")
    elif average >= 80:
        print(name + "is passing with an letter grade of B")
    elif average >= 70:
        print("*CAUTION* " + name + "is passing with an letter grade of C")
    elif average >= 60:
        print("*CAUTION* " + name + "is passing with an letter grade of D, but will not recieve credit points from the University")
    else:
        print("*CAUTION* " + "The student " + name + " is failing the class, Please reveiw with the student")
    print("______________________________________________________________________________________________________________________________")
    numOfgradesEntered = int(input("Please enter a number of grades you would like to enter professor!: "))

while numOfgradesEntered == 3:
    name = input("Please enter a students Name: ")
    if name == " ":
        print("No students name was entered!")
    
    grade1 = float(input("Please enter a grade for the students class work: "))
    grade2 = float(input("Please enter a grade for the students homework: "))
    grade3 = float(input("Please enter a third grade for the gradebook: "))


    sumOfallGrades = grade1+grade2+grade3
    average = sumOfallGrades/3

    print("The student " + name + " average is " + str(average))

    if average >= 90:
        print(name + "is passing with an letter grade of A")
    elif average >= 80:
        print(name + "is passing with an letter grade of B")
    elif average >= 70:
        print("*CAUTION* " + name + "is passing with an letter grade of C")
    elif average >= 60:
        print("*CAUTION* " + name + "is passing with an letter grade of D, but will not recieve credit points from the University")
    else:
        print("*CAUTION* " + "The student " + name + " is failing the class, Please reveiw with the student")
    print("______________________________________________________________________________________________________________________________")
    numOfgradesEntered = int(input("Please enter a number of grades you would like to enter professor!: "))

while numOfgradesEntered == 4:
    name = input("Please enter a students Name: ")
    if name == " ":
        print("No students name was entered!")
    
    grade1 = float(input("Please enter a grade for the students class work: "))
    grade2 = float(input("Please enter a grade for the students homework: "))
    grade3 = float(input("Please enter a third grade for the gradebook: "))
    grade4 = float(input("Please enter a third grade for the gradebook: "))


    sumOfallGrades = grade1+grade2+grade3
    average = sumOfallGrades/4

    print("The student " + name + " average is " + str(average))

    if average >= 90:
        print(name + "is passing with an letter grade of A")
    elif average >= 80:
        print(name + "is passing with an letter grade of B")
    elif average >= 70:
        print("*CAUTION* " + name + "is passing with an letter grade of C")
    elif average >= 60:
        print("*CAUTION* " + name + "is passing with an letter grade of D, but will not recieve credit points from the University")
    else:
        print("*CAUTION* " + "The student " + name + " is failing the class, Please reveiw with the student")
    print("______________________________________________________________________________________________________________________________")
    numOfgradesEntered = int(input("Please enter a number of grades you would like to enter professor!(2-5): "))
    


while numOfgradesEntered == 5:
    name = input("Please enter a students Name: ")
    if name == " ":
        print("No students name was entered!")
    
    grade1 = float(input("Please enter a grade for the students Attendance: "))
    grade2 = float(input("Please enter a grade for the students  quiz grade : "))
    grade3 = float(input("Please enter a grade for the student's test grade: "))
    grade4 = float(input("Please enter a grade for the student's midterm : "))
    grade5 = float(input("Please enter a grade for the student's final: "))

    sumOfallGrades = grade1+grade2+grade3+grade4+grade5
    average = sumOfallGrades/5

    print("The student " + name + " average is " + str(average))

    if average >= 90:
        print(name + "is passing with an letter grade of A")
    elif average >= 80:
        print(name + "is passing with an letter grade of B")
    elif average >= 70:
        print("*CAUTION* " + name + "is passing with an letter grade of C")
    elif average >= 60:
        print("*CAUTION* " + name + "is passing with an letter grade of D, but will not recieve credit points from the University")
    else:
        print("*CAUTION* " + "The student " + name + " is failing the class, Please reveiw with the student")
    print("______________________________________________________________________________________________________________________________")
    numOfgradesEntered = int(input("Please enter a number of grades you would like to enter professor!(2-5): "))
    
    
    
    
    

