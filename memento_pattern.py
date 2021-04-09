class Memento:
    def __init__(self, state: 'str'):
        self._state = state

    @property
    def state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = ''

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: 'str'):
        self._state = state

    def save_state_to_memnto(self):
        return Memento(self._state)

    def get_state_from_memento(self, memento: 'Memento'):
        self.state = memento.state


class CareTaker:
    memento_list = list()

    def add(self, state: 'Memento'):
        self.memento_list.append(state)

    def get(self, index: 'int'):
        return self.memento_list[index]


originator = Originator()
care_taker = CareTaker()
originator.state = 'state #1'
originator.state = 'state #2'
care_taker.add(originator.save_state_to_memnto())
originator.state = 'state #3'
care_taker.add(originator.save_state_to_memnto())
originator.state = 'state #4'

print(originator.state)
originator.get_state_from_memento(care_taker.get(0))
print(originator.state)
originator.get_state_from_memento(care_taker.get(1))
print(originator.state)
