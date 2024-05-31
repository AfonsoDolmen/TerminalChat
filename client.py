from blessed import Terminal
import socket
import threading


def receiveMessage(client_socket: socket.socket, terminal: Terminal) -> None:
    """
    Receive the message from the others clients

    :param client_socket: The client socket
    :param terminal: The terminal object

    :return: None
    """

    try:
        while True:
            # Receive and decode 1024 bytes from the server
            msg = client_socket.recv(1024).decode()

            # Moving the cursor to the top of the terminal and printing the messaged received
            with terminal.location(0, 0):
                print(terminal.clear_eol + f'says: {msg}')

    except Exception as e:
        print(e)
        # If there's an error to receive the message, the server must be off
        client_socket.close()
        raise Exception('Failed to receive the message!')


def sendMessage(client_socket: socket.socket, terminal: Terminal) -> None:
    """
    Move the cursor to a specific location and send the message

    :param client_socket: The socket of the client
    :param terminal: The terminal object

    :return: None
    """

    while True:
        try:
            # Moving the cursor to the bottom of the terminal and writing a message to send
            with terminal.location(0, terminal.height-1):
                client_socket.send(str(input('-> ')).encode())

        except Exception as e:
            print(e)
            # If there's an error to send the message, the server must be off
            client_socket.close()
            raise Exception('Error to send the message!')


def client() -> None:
    """
    Initialize the client and initialize the terminal

    :return: None
    """

    # Initialize the terminal and clearing the screen
    terminal = Terminal()
    print(terminal.clear)

    try:
        # Instantiate the client socket
        # IPV6 Family, TCP protocol
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connecting to the server
        host, port = 'localhost', 9000
        client_socket.connect((host, port))

        threading.Thread(target=sendMessage, args=(client_socket, terminal,)).start()
        threading.Thread(target=receiveMessage, args=(client_socket, terminal,)).start()

    except Exception as e:
        print(e)
        raise Exception('Error to connect to the server!')


if __name__ == '__main__':
    client()
