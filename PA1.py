 import os

##### Creating the CalUtils Object ########
class CalUtils:

    ######## Declaring Variables ######

    ##### Declare Empty Lists to store the names and heights of students ########
    names = []
    heights = []

    ##### Declare Variables to store total Height and total Count ########
    totalStudentHeight = 0
    totalStudentCount = 0

    ##### Creating the calAvgHeight Function for CalUtils Object ########
    def calAvgHeight(self):
        student = ""

        ######## File Operations #########

        ##### Open the file ########
        with open("listOfStudentHeight.txt", "r") as f:

            print("Read the first line")
            student = f.readline()

            ##### while there is text in the line ########
            while(len(student) > 0):
                ##### add one to the count of the students ########
                ##### remember to add self in front because you are using/modifying the object's properties ########
                self.totalStudentCount += 1

                ##### split the line into two (Student Name and Height) ########
                ##### Line is in the format : "Name Height" ########
                print(student)
                student_array = student.split()
                print("This Line is Split into: ", student_array)

                ##### remember to add self in front because you are using/modifying the object's properties ########
                self.names.append(student_array[0])
                print("Added ", student_array[0])
                self.heights.append(student_array[1])
                print("Added ", student_array[1])
                print("\n")

                ##### Add the current student height to the total height ########
                self.totalStudentHeight += float(student_array[1])

                ##### Read the Next Line ########
                print("Read the next line")
                student = f.readline()


        ##### Calculate the average ########
        ##### remember to add self in front because you are using/modifying the object's properties ########
        avg = self.totalStudentHeight / self.totalStudentCount

        print("\n")
        print("The Final List of Students is: ", self.names)
        print("The Final List of Heights is: ", self.heights)
        print("\n")
        print("The Student Count: ", self.totalStudentCount)
        print("The Student Total Height: ", self.totalStudentHeight)
        print("\n")

        ##### Two different ways of rounding off ########
        print("Rounding Method 1: Student average height is " + "{:.2f}".format(avg) + " for "+ str(self.totalStudentCount) + " students.")
        print("Rounding Method 2: Student average height is %.2f for %d students." %(avg, self.totalStudentCount))
        print("\n")

        ##### Getting the new student's Name and Heightdfs ########
        newName = input("Enter New Student Name:")
        newHeight = input("Enter New Student Height (in metres):")

        ##### try to catch any errors ########
        try:
            ##### Convert the user input into a float number ########
            newHeight = float(newHeight)

            ##### Add the new student data ########
            ##### remember to add self in front because you are using/modifying the object's properties ########
            self.names.append(newName)
            self.heights.append(newHeight)
            self.totalStudentCount += 1
            self.totalStudentHeight += newHeight

            ##### Recalculate the Average ########
            avg = self.totalStudentHeight / self.totalStudentCount
            print("Student average height is %.2f for %d students." % (avg, self.totalStudentCount))

        except ValueError:
            ##### If there is a ValueError (The user enters an invalid number, do this instead ########
            print("Invalid Height")


#### Create the CalUtils Object ####
cu = CalUtils()
#### Use the calAvgHeight function of the CalUtils Object ####
cu.calAvgHeight()

