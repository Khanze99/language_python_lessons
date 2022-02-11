

from abc import ABC, abstractmethod


class Command(ABC):
    """
    интерфейс комнады объявляет метод для выполнения команд
    """

    @abstractmethod
    def execute(self) -> None:
        pass


class Receiver:
    """
    Классы Получателей содержат некую важную бизнес-логику.
    Они умеют выполнять все виды опервций, связанных с выполнением запроса.
    Фактически, любой класс может выступать Получаетелем.
    """
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\n{self.__class__}: Also working on ({b}.)")


class SimpleCommand(Command):
    """
    некоторые команды способны выполнять простоые операции самостоятельно
    """

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"{self.__class__}: See, I can do simple things like printing\n({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b:str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print(f"{self.__class__}: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Invoker:
    """
    Отправитель связан с одной или несколькими командами. Он отправляет запрос
    """

    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print(f"{self.__class__}: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print(f"{self.__class__}: ... doing something really important...")

        print(f"{self.__class__}: Does anybody want something done before I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == '__main__':
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say HI!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "send email", "save report"))

    invoker.do_something_important()
