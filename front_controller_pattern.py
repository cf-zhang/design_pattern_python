class HomeView:
    def show(self):
        pass


class StudentView:
    def show(self):
        pass


class Dispatcher:
    def __init__(self):
        self.student_view = StudentView()
        self.home_view = HomeView()

    def dispatch(self, request: 'str'):
        if request == "student":
            self.student_view.show()
        else:
            self.home_view.show()


class FrontController:
    def __init__(self):
        self.dispatcher = Dispatcher()

    def is_authentic_user(self):
        print('user is authenticated successfully.')
        return True

    def track_request(self, request: 'str'):
        print('page requested ' + request)

    def dispatch_request(self, request: 'str'):
        self.track_request(request)
        if self.is_authentic_user():
            self.dispatcher.dispatch(request)


front_controller = FrontController()
front_controller.dispatch_request("home")
front_controller.dispatch_request("student")
