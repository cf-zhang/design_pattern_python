class AbstractCustomer:
    def __init__(self):
        self.name = ''

    def isNil(self):
        pass

    def get_name(self):
        pass

class RealCustomer(AbstractCustomer) :
    def __init__(self, name: 'str'):
        self.name = name

    def get_name(self):
        return self.name

    def isNil(self):
        return False

class NullCustomer(AbstractCustomer):
    def get_name(self):
        return 'Not available in customer database'

    def isNil(self):
        return True

class CustomerFactory:
    names = ['Rob', 'Joe', 'Julie']

    def get_customer(name: 'str'):
        for n in CustomerFactory.names:
            if n == name:
                return RealCustomer(name)
        return NullCustomer()

customer1 = CustomerFactory.get_customer('Rob')
customer2 = CustomerFactory.get_customer('aaa')
print(customer1.get_name())
print(customer2.get_name())

