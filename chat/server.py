from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor


class Client(Protocol):
    ip: str = None
    login: str = None
    factory: 'Chat'

    def __init__(self, factory):
        """
        Инициализация фабрики клиента
        :param factory:
        """

    def connectionMade(self):
        """
        Обработчик подключения нового клиента
        """

    def dataReceived(self, data: bytes):
        """
        Обработчик нового сообщения от клиента
        :param data:
        """

    def connectionLost(self, reason=None):
        """
        Обработчик отключения клиента
        :param reason:
        """


class Chat(Factory):
    clients: list

    def __init__(self):
        """
        Инициализация сервера
        """

    def startFactory(self):
        """
        Запуск процесса ожидания новых клиентов
        :return:
        """

    def buildProtocol(self, addr):
        """
        Инициализация нового клиента
        :param addr:
        :return:
        """

    def notify_all_users(self, data: str):
        """
        Отправка сообщений всем текущим пользователям
        :param data:
        :return:
        """


if __name__ == '__main__':
    reactor.listenTCP(7410, Chat())
    reactor.run()
