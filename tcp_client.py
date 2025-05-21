import socket


def start_tcp_client():
    """
    Start a TCP client that connects to the echo server, then sends a message
    and prints out the response from the server.
    """

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\
    
    server_address = ('localhost', 65432)
    print('Starting up on {} port {}'.format(*server_address))
    client_socket.connect(server_address)

    try:
        message = b'This is the message. It will be repeated.'
        print('Sending {!r}'.format(message))
        client_socket.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = client_socket.recv(16)
            amount_received += len(data)
            print('Received {!r}'.format(data))
    finally:
        print('Closing socket')
        client_socket.close()

# the lines below are our entrypoint - you can run this script by running
# `python tcp_client.py` from the command line.
if __name__ == "__main__":
    start_tcp_client()
