class Student:
    def __init__(self):
        self._name = ''
        self._rollNo = -1

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


class StudentView:
    def print_student_details(self, name, id):
        print('student: ')
        print('Name :' + str(name))
        print('id: ' + str(id))

class StudentController:
    def __init__(self, model: 'Student', view: 'StudentView'):
        self._model = model
        self._view = view

    def setStudentName(self, name):
        self._model.name = name

    def getStudentName(self):
        return self._model.name

    def setStudentRollNo(self, rollno):
        self._model.roll_no = rollno

    def getStudentRollNo(self):
        return self._model.roll_no

    def update_view(self):
        self._view.print_student_details(self._model.name, self._model.roll_no)

model = Student()
model.name = 'aaaa'
model.roll_no = 'bbbb'
view = StudentView()
controller = StudentController(model, view)
controller.update_view()