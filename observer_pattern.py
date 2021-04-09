class Subject:
    def __init__(self):
        self.observers = list()
        self.state = -1

    def get_state(self):
        return self.state

    def set_state(self, state: 'int'):
        self.state = state
        self.notify_all_observers()

    def attach(self, observer: 'Obersver'):
        self.observers.append(observer)

    def notify_all_observers(self):
        for observer in self.observers:
            observer.update()


class Observer:
    def __init__(self):
        self.subject = None

    def update(self):
        pass


class BinaryObserver(Subject):
    def __init__(self, subject: 'Subject'):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print('binary string : ' + str(self.subject.get_state()))


class Octalobserver(Subject):
    def __init__(self, subject: 'subject'):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print('octal string : ' + str(self.subject.get_state()))


class Hexobserver(Subject):
    def __init__(self, subject: 'subject'):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print('Hex string : ' + str(self.subject.get_state()))


subject = Subject()
Hexobserver(subject)
Octalobserver(subject)
BinaryObserver(subject)
subject.set_state(15)
subject.set_state(16)
