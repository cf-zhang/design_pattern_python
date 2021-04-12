class Service:
    def get_name(self):
        pass

    def execute(self):
        pass

class Service1(Service):
    def execute(self):
        print('executing sercice1')

    def get_name(self):
        return 'service1'


class Service2(Service):
    def execute(self):
        print('executing sercice2')

    def get_name(self):
        return 'service2'

class InitialContext:
    def lookup(self, name: 'str'):
        if name == 'service1':
            print('looking up and creating a new service 1')
            return Service1()
        elif name == 'service2':
            print('looking up and creating a new service 2')
            return Service2()
        return None

class Cache:
    def __init__(self):
        self.services = list()

    def get_service(self, service_name: 'str'):
        for x in self.services:
            if x.get_name() == service_name:
                print('returning cachec '+service_name+' object')
                return x
        return None
    def add_service(self, service: 'Service'):
        exists = False
        for x in self.services:
            if x.get_name() == service.get_name():
                exists = True
        if exists is False:
            self.services.append(service)

class ServiceLocator:
    cache = Cache()

    def get_service(name: 'str'):
        service = ServiceLocator.cache.get_service(name)
        if service is not None:
            return service

        context = InitialContext()
        service1 = context.lookup(name)
        ServiceLocator.cache.add_service(service1)
        return service1


service = ServiceLocator.get_service('service1')
service.execute()
service = ServiceLocator.get_service('service2')
service.execute()
service = ServiceLocator.get_service('service1')
service.execute()
service = ServiceLocator.get_service('service2')
service.execute()