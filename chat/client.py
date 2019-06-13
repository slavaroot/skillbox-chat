from twisted.internet import stdio, reactor
from twisted.internet.protocol import ClientFactory, Protocol


class DataWrapper(Protocol):
    output = None

    def dataReceived(self, data: bytes):
        """
        Вывод через канал клиента
        :param data:
        :return:
        """


class UserProtocol(DataWrapper):
    def wrap_input(self):
        """
        Передача управления ввода
        :return:
        """

    def connectionMade(self):
        """
        Обработчик успешного соединения
        :return:
        """


class UserFactory(ClientFactory):
    protocol = UserProtocol
    login: str

    def __init__(self, user_login: str):
        """
        Инициализация клиента
        :param user_login:
        """

    def startedConnecting(self, connector):
        """
        Установка соединения
        :param connector:
        :return:
        """

    def clientConnectionLost(self, connector, reason):
        """
        Обработчик отключения сервера
        :param connector:
        :param reason:
        :return:
        """

    def clientConnectionFailed(self, connector, reason):
        """
        Обработчик неудачного соединения
        :param connector:
        :param reason:
        :return:
        """


if __name__ == '__main__':
    login = input("Your login >>> ")
    reactor.connectTCP(
        "localhost",
        7410,
        UserFactory(login)
    )
    reactor.run()
