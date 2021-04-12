class DependentObject1:
    def __init__(self):
        self.data_ = None

    @property
    def data(self):
        return self.data_

    @data.setter
    def data(self, data: 'str'):
        self.data_ = data


class DependentObject2:
    def __init__(self):
        self.data_ = None

    @property
    def data(self):
        return self.data_

    @data.setter
    def data(self, data: 'str'):
        self.data_ = data

class CoarseGrainedObject:
    def __init__(self):
        self.do1 = DependentObject1()
        self.do2 = DependentObject2()

    def set_data(self, data1: 'str', data2: 'str'):
        self.do1.data = data1
        self.do2.data = data2

    def get_data(self):
        return [self.do1, self.do2]

class CompositeEntity:
    def __init__(self):
        self.cgo = CoarseGrainedObject()

    def set_data(self, data1: 'str', data2: 'str'):
        self.cgo.set_data(data1, data2)

    def get_data(self):
        return self.cgo.get_data()

class Client:
    def __init__(self):
        self.composite_entity = CompositeEntity()

    def print_data(self):
        for x in self.composite_entity.get_data():
            print('data: ' + x.data)

    def set_data(self, data1: 'str', data2: 'str'):
        self.composite_entity.set_data(data1, data2)

client = Client()
client.set_data('test', 'data')
client.print_data()
client.set_data('second', 'data1')
client.print_data()





