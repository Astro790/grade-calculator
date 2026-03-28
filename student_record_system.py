import json
class Student:
    def __init__(self):
        self.name = ""
        self.no_of_courses = 0
        self.student_db = {}
        self.temporary_db = []
        self.filefound = None

        
    def getDetails(self):
            '''This function gets the student name, number of courses offered by the student calculate
            the student grade,scores,unit and they are stored in a list'''
            self.name = input("Enter student name: ")
            while True:
                try:
                   self.no_of_courses = int(input(f"Enter the number of courses {self.name} is offering: "))
                   break
                except ValueError:
                    print("ERROR!!\n ACCEPTS ONLY INTEGERS") 
            courses = []
            for i in range(self.no_of_courses):
                course_data ={}
                course = input("Enter the name of the course: ")
                while True:
                   try:
                      score = float(input("Enter your score: "))
                      break
                   except ValueError:
                    print("ERROR!!\nACCEPTS ONLY NUMBERS")
                while True:
                    try:
                      unit = int(input(f"How many unit is {course}: "))
                      break
                    except ValueError:
                        print("ERROR!!\nACCEPTS ONLY INTEGERS")
                course_data["course"] = course.title()
                course_data["score"] = score
                course_data["units"] = unit
                if score >= 80:
                    course_data["grade"] = "A"
                    course_data["course point"] = 5 * unit
                elif score>= 60 and score <=79:
                    course_data["grade"] = "B"
                    course_data["course point"] = 4 * unit
                elif score>=50 and score<=59:
                    course_data["grade"] = "C"
                    course_data["course point"] = 3 * unit
                elif score>=40 and score<=49:
                    course_data["grade"] = "D"
                    course_data["course point"] = 2 * unit
                elif score>=30 and score<=39:
                    course_data["grade"] = "E"
                    course_data["course point"] = 1 * unit
                elif score<30:
                    course_data["grade"] = "F"
                    course_data["course point"] = 0 * unit
                if score>= 50:
                    course_data["status"] = "PASSED"
                else:
                    course_data["status"] = "FAILED"
                courses.append(course_data)
            self.student_db = {
                "name" : self.name.title(),
                "courses" : courses
            }

        
    def Calculategpa(self):
        '''This functions gets the student score, unit,total scores and uses them
        to find the student GPA and Average score and saves it back to the list'''
        total_unit=total_score=total_available_unit=total_points=passed=failed=0
        course_list = self.student_db['courses']
        for course in course_list:
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
        average = total_score/self.no_of_courses
        gpa = round(total_points/total_unit,2)
        student_data = {'GPA' : gpa,
                         'AVERAGE SCORE' : average, 
                        'NUMBER OF PASSED COURSE' : passed,
                        'NUMBER OF FAILED COURSE' : failed
                        }
        self.student_db.update(student_data)

            
    def save(self):
        '''This function creates a JSON file if it doesnt exist and saves al the data in the list 
        to the JSON file so that even after the proram closes it can stil be accessed when the program
        starts again'''
        try:
            with open('Student_database.JSON','r') as database_file:
                student_db = json.load(database_file)
        except FileNotFoundError:
            with open('Student_database.JSON', 'w') as database_file:
                student_db = []
        student_db.append(self.student_db)
        with open('Student_database.JSON','w') as database_file:
            json.dump(student_db,database_file,indent = 3)
        

    
    def load(self):
        '''This is the function that helps us load the JSON file into the program'''
        temporary_db = []
        try:
            with open('Student_database.JSON', 'r') as database_file:
                temporary_db = json.load(database_file)
                self.filefound= True

        except FileNotFoundError:
            print("FILE DOES NOT EXIST")
            self.filefound = False
        self.temporary_db = temporary_db
        if len(self.temporary_db) == 0:
             print("NO STUDENT IN FILE")
             self.filefound = False
            

    

    def AddStudent(self):
        '''This function is responsible for adding students to the JSON file'''
        self.getDetails()
        self.Calculategpa()
        self.save()

    
    def DisplayStudent(self):
        '''This function loads students data from the JSON file  and display all the 
        student data stored in the JSON file'''
        self.load()
        if self.filefound:
          print("_"*30 + "STUDENT PERFOMANCE SUMMARY" + "_"*30)
          for student in self.temporary_db:
            print("-"*20 + f"{student['name'].upper()}" +" PERFORMANCE" + "-"*20)
            print(f"NAME: {student['name'].upper()}")
            print(f"GPA: {student['GPA']}")
            print(f"NUMBER OF COURSES PASSED: {student['NUMBER OF PASSED COURSE']}")
            print(f"NUMBER OF COURSES FAILED: {student['NUMBER OF FAILED COURSE']}\n")


    def SearchforStudent(self):
        '''This function searches for student in the JSON file and brings out the information 
        of the student that was searched for'''
        student_found=False
        self.load()
        if self.filefound:
             name = input("Enter student name: ")
             for student in self.temporary_db:
                if name.lower() == student['name'].lower():
                    student_found=True
                    print(f"NAME: {student['name'].upper()}")
                    print(f"GPA: {student['GPA']}") 
                    courses = student['courses']
                    for course in courses:
                       print(f"-------------{course['course'].upper()} detail----------------")
                       print(f"{course['course'].upper()} UNIT: {course['units']}")
                       print(f"{course['course'].upper()} POINTS: {course['course point']}")
                       print(f"SCORE: {course['score']}")
                       print(f"GRADE: {course['grade']}")
                       print(f"STATUS: {course['status']}")
                    print(f"NUMBER OF COURSES PASSED: {student['NUMBER OF PASSED COURSE']}")
                    print(f"NUMBER OF COURSES FAILED: {student['NUMBER OF FAILED COURSE']}")
             if not student_found:
               print(f"{name.upper()} DOES NOT EXIST")


    def UpdateStudentScore(self):

        self.load()
        if self.filefound:
              student_found=course_found = False
              name = input("Enter the student you want to update there details: ")
              for s in self.temporary_db:

                if name.lower() == s['name'].lower():
                   position = self.temporary_db.index(s)
                   student_found = True
                   print(f"{name.upper()} FOUND")
                   courses = s['courses']
                   course_name = input("Enter the course u want to change grade: ")
                   for course in courses:
                       if course_name.lower() == course['course'].lower():
                           course_found = True
                           new_score = int(input(f"Enter new score of {s['name'].upper()} in {course['course']}: "))
                           course['score'] = new_score
                           unit = course['units']
                           if new_score >= 80:
                                course["grade"] = "A"
                                course["course point"] = 5 * unit
                           elif new_score>= 60 and new_score <=79:
                                course["grade"] = "B"
                                course["course point"] = 4 * unit
                           elif new_score>=50 and new_score<=59:
                                course["grade"] = "C"
                                course["course point"] = 3 * unit
                           elif new_score>=40 and new_score<=49:
                                course["grade"] = "D"
                                course["course point"] = 2 * unit
                           elif new_score>=30 and new_score<=39:
                                course["grade"] = "E"
                                course["course point"] = 1 * unit
                           elif new_score<30:
                                course["grade"] = "F"
                                course["course point"] = 0 * unit
                           if new_score>= 50:
                                course["status"] = "PASSED"
                           else:
                                course["status"] = "FAILED"
                   break
              if student_found:
                 self.no_of_courses = len(courses)
                 self.temporary_db = [s for s in self.temporary_db if name.lower() != s['name'].lower()]
                 self.student_db = s
                 self.Calculategpa()
                 self.temporary_db.insert(position,self.student_db)
                 with open('Student_database.JSON', 'w') as Database:
                     json.dump(self.temporary_db,Database,indent = 3)
                 print(f"{name.upper()} UPDATED SUCESSFULLY")
              if  not student_found:
                print(f"{name.upper()} NOT FOUND")
              elif not course_found:
                 print(f"{course_name.upper()} NOT FOUND")


               
                
                    

    def DeleteStudent(self,name,message):
        '''This program searches for students that we want to remove from the program'''
        self.load()
        if self.filefound:
             new_db = []
             student_found =False
             for student in self.temporary_db:
                 if name.lower() == student['name'].lower():
                     student_found = True
                 else:
                   new_db.append(student)
             if student_found:
                 with open('Student_database.JSON','w') as database_file:
                     json.dump(new_db,database_file,indent = 3)
                 if message:
                    print(f"{name.upper()} has been removed sucessfully")
             else:
              print(f"{name.upper()} does not exist")
            

choice = 0
s = Student()
while choice != 6:
    while True:
      try:
        choice = int(input("1. ADD STUDENT\n2. VIEW ALL STUDENTS\n3. SEARCH FOR A STUDENT\n4. DELETE A STUDENT\n5. UPDATE STUDENT SCORE\n6. EXIT\nENTER YOUR OPTION: "))
        break
      except  ValueError:
        print("ENTER ONLY INTEGER VALUE")
    if choice == 1:
        s.AddStudent()
    elif choice == 2:
        s.DisplayStudent()
    elif choice == 3:
        s.SearchforStudent()
    elif choice == 4:
        name =input("Enter the student name u want to remove: ")
        s.DeleteStudent(name,message=True)
    elif choice == 5:
        s.UpdateStudentScore()
    elif choice == 6:
        print("YOU HAVE EXITED THE PROGRAM")
    else:
        print("ENTER A VALID CHOICE")