class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

student1 = Student("Katarzyna Lubnauer", [60, 70, 80])
student2 = Student("Tomasz Ćwiąkała", [40, 30, 20])

print(student1.is_passed())  
print(student2.is_passed()) 