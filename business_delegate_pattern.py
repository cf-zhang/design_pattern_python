class BusinessService:
    def do_processing(self):
        pass


class EJBService(BusinessService):
    def do_processing(self):
        print('processing task by invoking EJB service')


class JMSService(BusinessService):
    def do_processing(self):
        print('processing task by invoking JMS Service')


class BusinessLookUp:
    def get_business_service(self, service_type: 'str'):
        if service_type == 'EJB':
            return EJBService()
        else:
            return JMSService()


class BusinessDelegate:
    def __init__(self):
        self.lookup_service = BusinessLookUp()
        self.service_type = None
        self.business_service = None

    def set_service_type(self, service_type: 'str'):
        self.service_type = service_type

    def do_task(self):
        self.business_service = self.lookup_service.get_business_service(self.service_type)
        self.business_service.do_processing()


class Client:
    def __init__(self, business_service: 'BusinessDelegate'):
        self.business_service = business_service

    def do_task(self):
        self.business_service.do_task()


business_delegate = BusinessDelegate()
business_delegate.set_service_type('EJB')

client = Client(business_delegate)
client.do_task()
business_delegate.set_service_type('JMS')
client.do_task()
