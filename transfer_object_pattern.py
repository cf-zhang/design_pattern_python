class StudentVO:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_rollno(self):
        return self.rollno

    def set_rollno(self, rollno):
        self.rollno = rollno

class StudentBO:
    def __init__(self):
        self.students = [StudentVO('Robert', 0), StudentVO('John', 1)]

    def delete_student(self, student: 'StudentVO'):
        self.students.remove(student)

    def get_all_students(self):
        return self.students

    def get_student(self, rollno):
        for x in self.students:
            if x.get_rollno() == rollno:
                return x

    def update_student(self, student: 'StudentVO'):
        for x in self.students:
            if x.get_rollno() == student.rollno:
                x.name = student.name
            print('name: '+x.name+'is updated')

student_business_object = StudentBO()

for s in student_business_object.get_all_students():
    print(s.name)