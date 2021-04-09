class User:
    def __init__(self, name: 'str'):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: 'str'):
        self._name = name

    def send_message(self, message: 'str'):
        ChatRoom.show_message(self, message)


class ChatRoom:
    def show_message(user: 'User', message: 'str'):
        print('[' + user.name + ']: ' + message)


robert = User('Robert')
john = User('John')

robert.send_message('Hi! John!')
john.send_message('Hello! Robert')
