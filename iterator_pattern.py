class Iterator:
    def has_next(self):
        pass

    def next(self):
        pass

class Container:
    def get_iterator(self):
        pass

class NameRespository(Container):
    names = ['Robert', 'John', 'Julie', 'Lora']
    class NameIterator(Iterator) :
        def __init__(self):
            self.index = 0

        def has_next(self):
            if len(NameRespository.names) > self.index:
                return True
            return False
        def next(self):
            if self.has_next():
                name = NameRespository.names[self.index]
                self.index += 1
                return name
            return None

    def get_iterator(self):
        return self.NameIterator()


name_reposity = NameRespository()
iter = name_reposity.get_iterator()
while iter.has_next():
    print(iter.next())