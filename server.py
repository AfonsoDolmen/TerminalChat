import socket
import threading

# Creating a list to all the users connected
users = list()


def sendMessageToAllClients(client_socket: socket.socket, msg: str) -> None:
    """
    Send the message received from the client for all the clients connected

    :param client_socket: The client socket
    :param msg: The message to send

    :return: None
    """

    try:
        # Send the message to all clients connected
        for user in users:
            user.send(msg.encode())

    except Exception as e:
        print(e)
        # If there's an error, the client must be disconnected
        client_socket.close()
        raise Exception('Failed to send the message to client!')


def receiveMessage(client_socket: socket.socket, addr: str) -> None:
    """
    Receive a message from the connect client

    :param client_socket: The client socket
    :param addr: the address of the connect client

    :return: None
    """
    try:
        while True:
            # Receive and decode 1024 bytes from the client
            msg = client_socket.recv(1024).decode()

            # Just debugging
            print(f'{addr[0]} says: {msg}')

            # If there's a message, so send it!
            if msg:
                sendMessageToAllClients(client_socket, msg)

    except Exception as e:
        print(e)
        # If there's an error to receive, the client must be disconnected
        client_socket.close()
        raise Exception('Failed to receive the message!')


def server() -> None:
    """
    Initialize the server

    :return: None
    """

    # Instantiate the socket
    # IPV4 Family, TCP protocol
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the host and port to the socket
        host, port = 'localhost', 9000
        server_socket.bind((host, port))

        # Listen for any connections and push to the queue
        server_socket.listen()

        print('Server running!')

        while True:
            # Accept the connection and pop from the queue
            client_socket, addr = server_socket.accept()

            # When a client connect, the socket it added to the list
            users.append(client_socket)

            print(f'{addr[0]} has connected to the server!')

            # Receive the messages
            threading.Thread(target=receiveMessage, args=(client_socket, addr,)).start()

    except Exception as e:
        print(e)
        server_socket.close()
        raise Exception('Error to initialize the server!')


if __name__ == '__main__':
    server()
