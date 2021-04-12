class Student:
    def __init__(self, name: 'str', id: 'int'):
        self._name = name
        self._rollNo = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def roll_no(self):
        return self._rollNo

    @roll_no.setter
    def roll_no(self, roll_no):
        self._rollNo = roll_no

class StudentDao:
    def get_all_students(self):
        pass
    def get_student(self, roll_no: 'int'):
        pass
    def update_student(self, student: 'Student'):
        pass
    def delete_student(self, student: 'Student'):
        pass

class StudentDapImpl(StudentDao):
    def __init__(self):
        self.students = [Student("Robert", 0), Student("John", 1)]

    def delete_student(self, student: 'Student'):
        self.students.remove(student)

    def get_all_students(self):
        return self.students

    def get_student(self, roll_no: 'int'):
        for x in self.students:
            if x.roll_no == roll_no:
                return x

    def update_student(self, student: 'Student'):
        for x in self.students:
            if x.roll_no == student.roll_no:
                x.name = student.name
        print('update roll_no: '+str(student.roll_no))

student_dao = StudentDapImpl()
for x in student_dao.get_all_students():
    print("name: "+ str(x.name))





