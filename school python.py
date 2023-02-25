class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class School:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, grade):
        student = Student(name, grade)
        self.students.append(student)
        print(f"{name} has been added to the school database.")
    
    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"{name} has been removed from the school database.")
                return
        print(f"Student '{name}' not found in the school database.")
    
    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                print(f"Name: {student.name}, Grade: {student.grade}")
                return
        print(f"Student '{name}' not found in the school database.")
    
    def get_all_students(self):
        if not self.students:
            print("No students in the school database.")
            return
        for student in self.students:
            print(f"Name: {student.name}, Grade: {student.grade}")
    
    def update_grade(self, name, new_grade):
        for student in self.students:
            if student.name == name:
                student.grade = new_grade
                print(f"Grade updated for {name}. New grade: {new_grade}")
                return
        print(f"Student '{name}' not found in the school database.")

# Example usage
school = School()
school.add_student("John", 9)
school.add_student("Jane", 10)
school.get_all_students()
school.get_student("John")
school.update_grade("John", 10)
school.remove_student("Jane")
