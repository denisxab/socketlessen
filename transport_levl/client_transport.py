import socket
from typing import Final


class TcpClient:
    EXIT: Final[str] = "!exit"

    def __init__(self, type_net: int):
        """
        type_net: Транспортный уровень
            - socket.AF_UNIX = uds
            - socket.AF_INET = ipv4
            - socket.AF_INET6 = ipv6
        """
        # Размер сообщения
        self.SIZE_CONTENT = 1024
        # Настройка socket
        self.client_socket = socket.socket(family=type_net, type=socket.SOCK_STREAM)

    def disconnect(self):
        self.client_socket.send(self.EXIT.encode("utf-8"))  # Уведомить сервер об отключении
        self.client_socket.close()


class UdpClient:
    def __init__(self, type_net: int):
        """
        type_net: Транспортный уровень
            - socket.AF_UNIX = uds
            - socket.AF_INET = ipv4
            - socket.AF_INET6 = ipv6
        """
        # Размер сообщения
        self.SIZE_CONTENT = 1024
        # Настройка socket
        self.client_socket = socket.socket(family=type_net, type=socket.SOCK_DGRAM)
