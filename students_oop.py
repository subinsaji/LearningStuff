class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 to 100

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name 
        self.max_students = max_students
        self.students = []
    
    def add_student(self, students):
        if len(self.students) < self.max_students:
            self.students.append(students)
            return True 
        return False
    
    def get_average_grade(self):
        pass



