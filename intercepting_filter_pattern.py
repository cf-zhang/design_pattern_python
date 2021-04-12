class Filter:
    def execute(self, request: 'str'):
        pass


class AuthenticationFilter(Filter):
    def execute(self, request: 'str'):
        print('authenticating request ' + request)


class DebugFilter(Filter):
    def execute(self, request: 'str'):
        print('request log :' + request)


class Target:
    def execute(self, request: 'str'):
        print('executing request: ' + request)


class FilterChain:
    def __init__(self):
        self.filters = list()
        self.target = Target()

    def add_filter(self, filter: 'Filter'):
        self.filters.append(filter)

    def execute(self, request: 'str'):
        for filter in self.filters:
            filter.execute(request)
        self.target.execute(request)

    def set_target(self, target: 'Target'):
        self.target = target


class FilterManager:
    def __init__(self, target: 'Target'):
        self.filter_chain = FilterChain()
        self.filter_chain.set_target(target)

    def set_filter(self, filter: 'Filter'):
        self.filter_chain.add_filter(filter)

    def filter_request(self, request: 'str'):
        self.filter_chain.execute(request)


class Client:
    def __init__(self):
        self.filter_manager = None

    def set_filter_manager(self, filter_manager: 'FilterManager'):
        self.filter_manager = filter_manager

    def send_request(self, request: 'str'):
        self.filter_manager.filter_request(request)


filter_manager = FilterManager(Target())
filter_manager.set_filter(AuthenticationFilter())
filter_manager.set_filter(DebugFilter())

client = Client()
client.set_filter_manager(filter_manager)
client.send_request('home')
