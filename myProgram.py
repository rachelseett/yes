import os

class CalUtils:
    names = []
    heights = []
    totalStudentHeight = 0;
    totalStudentCount = 0;

    def calAvgHeight(self):
        student = "start"

        ######## File Operations #####
        with open("listOfStudentHeight.txt", "r") as f:
            while(len(student) > 0):
                student = f.readline()
                self.totalStudentCount += 1
                student_array = student.split(" ")
                cnt = 0
                for x in student_array:
                    if len(x) > 0:
                        if cnt == 0:
                            self.names.append(x)
                            cnt = 1
                        else:
                            x = x.replace("\n", "")
                            self.heights.append(float(x))
                            self.totalStudentHeight += float(x)
                            cnt = 0

        avg = self.totalStudentHeight / self.totalStudentCount
        print("Student average height is " + "{:.2f}".format(avg) + " for "+ str(self.totalStudentCount) + " students.")
        print("Student average height is %.2f for %d students." %(avg, self.totalStudentCount))
        print(self.names)
        print(self.heights)
        newName = input("Enter New Student Name:")
        newHeight = input("Enter New Student Height (in metres):")

        try:
            float(newHeight)
        except ValueError:
            print("Invalid Height")

        newHeight = float(newHeight)
        if type(newHeight) == float:
            self.names.append(newName)
            self.heights.append(newHeight)
            self.totalStudentCount += 1
            self.totalStudentHeight += newHeight

            avg = self.totalStudentHeight / self.totalStudentCount
            print("Student average height is %.2f for %d students." % (avg, self.totalStudentCount))

cu = CalUtils()
cu.calAvgHeight()

