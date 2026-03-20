def getDetails(no_of_courses,student_db):
    ''' This functions gets the user score and unit of each course they offer and stores them in 
    a dictionary and each dictionary is then added to the list(student_db)
    ''' 
    i = 0
    while i<no_of_courses:
        course = input("Enter the name of the course: ")
        score = float(input("Enter your score: "))
        unit = int(input(f"How many unit is {course}: "))
        student_course = {}
        student_course["course"] = course
        student_course["score"] = score
        student_course["units"] = unit
        student_db.append(student_course)
        i += 1
    return student_db


def grade_and_pointCalculator(student_db):
    '''This function gets the score from the list and thn use the score
    to calculate the user grade and unit for each course and adds them to
     there repective dictionary'''
    for course in student_db:
        score = course["score"]
        unit = course["units"]
        if score >= 80:
            course["grade"] = "A"
            course["course point"] = 5 * unit
        elif score>= 60 and score <=79:
            course["grade"] = "B"
            course["course point"] = 4 * unit
        elif score>=50 and score<=59:
            course["grade"] = "C"
            course["course point"] = 3 * unit
        elif score>=40 and score<=49:
            course["grade"] = "D"
            course["course point"] = 2 * unit
        elif score>=30 and score<=39:
            course["grade"] = "E"
            course["course point"] = 1 * unit
        elif score<30:
            course["grade"] = "F"
            course["course point"] = 0 * unit
        if score>= 50:
            course["status"] = "PASSED"
        else:
            course["status"] = "FAILED"
    return student_db


def displayCourseDetail(student_db):
    '''This function displays all courses offered by the user
    and the scores,grade,units of the courses'''
    for courses in student_db:
        course_name = courses.get("course")
        scores = courses.get("score")
        student_status = courses.get("status")
        grade = courses.get("grade")
        points = courses.get("course point")
        unit = courses.get("units")
        print(f"Course: {course_name}")
        print(f"COURSE UNIT: {unit}")
        print(f"SCORE: {scores}")
        print(f"GRADE: {grade}")
        print(f"UNIT POINTS: {points}")
        print(f"YOU {student_status.upper()} {course_name}")
        print("-----------------------------------------\n")


def displayStudentPerformance(student_db,no_of_courses):
    '''This function calculates students gpa average score and displays the summary of 
    the users performance'''
    total_unit=total_points=total_available_unit=total_score=passed=failed=0
    for course in student_db:
        score = course.get("score")
        points = course.get("course point")
        units = course.get("units")
        status = course.get("status")
        max_unit = units * 5
        total_unit += units
        total_available_unit += max_unit
        total_score += score
        total_points += points
        if status == "PASSED":
            passed += 1
        elif status == "FAILED":
            failed += 1
    average = total_score/no_of_courses
    gpa = total_points/total_unit
    print("----------------STUDENT OVERALL PERFORMANCE----------------")
    print(f"TOTAL UNITS: {total_unit}")
    print(f"TOTAL POINTS: {total_points}/{total_available_unit}")
    print(f"GPA: {gpa}")
    print(f"AVERAGE SCORE: {average}")
    print(f"YOU PASSED {passed} COURSES")
    print(f"YOU FAILED {failed} COURSES")



no_of_courses = int(input("How many courses are you offering "))
student_db = getDetails(no_of_courses,student_db = [])
student_db =  grade_and_pointCalculator(student_db)
print(student_db)
displayCourseDetail(student_db)
displayStudentPerformance(student_db,no_of_courses)