class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __str__(self):
        return self.first + " " + self.last

class Employee(Person):
    def __init__(self, first, last, staffNum):
        super().__init__(first, last)
        self.staffNum = staffNum
    
    def __str__(self):
        return super().__str__() + " " + str(self.staffNum)  # Convert staffNum to string

person = Person("Merge", "Simpson")
employee = Employee("Homer", "Simpson", 2024)  # Note: staffNum should be an integer, not a string

print(person)
print(employee)