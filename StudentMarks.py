class Student:
    def __init__(self, name, m1, m2):
        self.name = name  # Initialize name
        self.m1 = m1      # Initialize marks for UT1
        self.m2 = m2      # Initialize marks for UT2

    def setName(self, name):
        self.name = name  # Method to set name
    
    def getName(self):
        return self.name  # Method to get name
    
    def setMarks(self, m1, m2):
        self.m1 = m1  # Method to set marks for UT1
        self.m2 = m2  # Method to set marks for UT2
    
    def getMarks(self):
        return self.m1, self.m2  # Method to get marks for both UTs
    
    def cal_avg(self):
        self.avg = (self.m1 + self.m2) / 2  # Method to calculate average marks
        
    def cal_grade(self):
        # Method to calculate grade based on average marks
        if self.avg >= 16:
            self.grade = 'A'
        elif 12 <= self.avg <= 15:
            self.grade = 'B'
        else:
            self.grade = 'C'
    
    def display_info(self):
        # Method to display student information
        print(self.name, self.avg, self.grade)


# Create a list to store student objects
students = []

# Loop to input details for multiple students
for i in range(5):
    name = input("Enter name of student: ")
    marks1 = int(input("Enter UT1 marks: "))
    marks2 = int(input("Enter UT2 marks: "))
    
    # Create a student object with provided details
    student = Student(name, marks1, marks2)
    
    # Calculate average and grade for the student
    student.cal_avg()
    student.cal_grade()
    
    # Add the student object to the list
    students.append(student)

# Display information for all students
for student in students:
    student.display_info()
