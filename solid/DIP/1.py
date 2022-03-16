from abc import abstractmethod


class IService:

    @abstractmethod
    def makeSvc(self):
        pass


class IServiceFactory(IService):
    def makeSvc(self):
        return ConcreteImpl()


class ServiceFactoryImpl(IServiceFactory):
    pass


class ConcreteImpl:
    pass


class Application:

    def __init__(self, service: ServiceFactoryImpl):
        self.service = service

    def __getattr__(self, item):
        if item == 'makeSvc':
            return getattr(self.service, item)
