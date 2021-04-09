class State:
    def doAction(self, context: 'Context'):
        pass

class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state: 'State'):
        self.state = state

    def get_state(self):
        return self.state

class StartState(State):
    def doAction(self, context: 'Context'):
        print('this is in start state')
        context.set_state(self)

    def __str__(self):
        return "start state"


class StopState(State):
    def doAction(self, context: 'Context'):
        print('this is in stop state')
        context.set_state(self)

    def __str__(self):
        return "stop state"

context = Context()
start_state = StartState()
start_state.doAction(context)
print(context.get_state())
stop_state = StopState()
stop_state.doAction(context)
print(context.get_state())
