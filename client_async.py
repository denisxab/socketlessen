from asyncsocket.client_async import ClientIpAsync
from general_settings import port, host

if __name__ == '__main__':
    message = ''
    while message != "exit":
        message = input(":::")
        ClientIpAsync(
            host=host,
            port=port
        ).send(
            message_to_server=message,
            send_to_server=ClientIpAsync.base_send_to_server,
        )
