class Students:
    def __init__(self, name):
        self.name = name
        self.grades = []
    

    def add_grades(self, grade):
        self.grades.append(grade)
        #print(f"{self.name} — QO'shildi! ")


    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def result(self):
        if self.average_grade()>= 4:
            print(f"{self.name} — O'tdi")
        else:
            print(f"{self.name} — O'tmadi")

talaba1 = Students("Jasur")
talaba1.add_grades(5)
talaba1.add_grades(4)
talaba1.add_grades(5)
talaba1.add_grades(5)
talaba1.add_grades(4)


talaba2 = Students("Malika")
talaba2.add_grades(3)
talaba2.add_grades(5)
talaba2.add_grades(4)
talaba2.add_grades(5)
talaba2.add_grades(4)



talaba3 = Students("Sardor")
talaba3.add_grades(4)
talaba3.add_grades(5)
talaba3.add_grades(3)
talaba3.add_grades(4)
talaba3.add_grades(5)


talaba4 = Students("Nilufar")
talaba4.add_grades(3)
talaba4.add_grades(5)
talaba4.add_grades(5)
talaba4.add_grades(5)
talaba4.add_grades(4)


talaba5 = Students("Ali")
talaba5.add_grades(5)
talaba5.add_grades(5)
talaba5.add_grades(5)
talaba5.add_grades(5)
talaba5.add_grades(4)


talabalar = [talaba1, talaba2, talaba3, talaba4, talaba5]

for student in talabalar:
    student.result()

print(talaba3.average_grade())