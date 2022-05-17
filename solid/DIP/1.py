"""
Application использует кокнретную реализацию Concreteimpl через интерфейс Service.
Однако приложению требуется каким-то образом создавать экземпляры ConcreteImpl.
Чтобы решить эту задачу бещ образования зависимости от ConcreteImpl на уровне исходного кода,
приложение вызывает метод make_svc интерфейса фабрики ServiceFactory. Этот  метод реализован в классе
ServiceFactoryImpl, наследующем ServiceFactory. Эта реализация создает экземпляр ConcreteImpl и возвращает его
как экземпляр интерфейса Service
"""


from abc import abstractmethod


class IService:
    pass


class ConcreteImpl(IService):
    pass


class IServiceFactory(IService):
    @abstractmethod
    def make_svc(self) -> IService:
        pass


class ServiceFactoryImpl(IServiceFactory):
    def make_svc(self) -> ConcreteImpl:
        return ConcreteImpl()


class Application:

    def __init__(self, concrete_impl: ConcreteImpl):
        self.concrete_impl = concrete_impl


if __name__ == '__main__':
    service_factory = ServiceFactoryImpl()
    concrete_impl = service_factory.make_svc()
    app = Application(concrete_impl)
