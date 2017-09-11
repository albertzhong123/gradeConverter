def grade_converter(grade):
    if (grade>=88 and grade <= 100):
        return 'A'
    if (grade>=80):
        return 'B'
    if (grade>=67):
        return 'C'
    if (grade>=60):
        return 'D'
    else:
        return 'F'

def gpaCreator(courses):
    courseList = []
    initialSum = 0
    for i in range(courses):
        grade = input("Please enter your grade: ")
        courseList.append(grade)
    for j in range(len(courseList)) :
        if (courseList[j].lower() == 'a'):
            initialSum += 4
        elif (courseList[j].lower() == 'b'):
            initialSum += 3
        elif (courseList[j].lower() =='c'):
            initialSum += 2
        elif (courseList[j].lower() == 'd'):
            initialSum +=1
        elif (courseList[j].lower() == 'f'):
            initialSum +=0
        else:
            newGrade = input("Please enter a valid grade: ")
            courseList[j] = newGrade
    return initialSum/courses

def main():
    decision = 'y'
    while (decision.lower() == 'y'):
        choice = int(input("grade or GPA (1/2): "))
        if (choice == 1):
            grade = int(input("Please enter your numerical grade: "))
            print ("Letter grade:" + grade_converter(grade))
            response = input("Continue?(y/n): ")
            while (response.lower() =='y'):
                if (response.lower() == 'y'):
                    gradeAgain = int(input("Please enter your numerical grade: "))
                    print ("Letter grade:" + grade_converter(gradeAgain))
                    response = input("Continue?(y/n): ")
                else:
                    print ("Bye!")
        elif (choice == 2):
            courses = int(input("Please enter the number of courses: "))
            print ("Your gpa is:",gpaCreator(courses))
        decision = input("Would you like to continue?(y/n): ")
    print ("Have a nice day!")
        
if (__name__ == "__main__"):
    main()


