import socket
import threading

def handle_client(connection, client_address):
    try:
        print('Connection from', client_address)
        while True:
            data = connection.recv(16)
            if data:
                print('Received {!r}'.format(data))
                connection.sendall(data)
            else:
                print('No more data from', client_address)
                break
    finally:
        connection.close()


def start_threaded_tcp_server():
    """
    Start a TCP server that listens for incoming requests and echoes back what
    it receives.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print('Waiting for a connection')

    while True:
        connection, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(connection, client_address))
        client_thread.start()


# the lines below are our entrypoint - you can run this script by running
# `python tcp_server.py` from the command line.
if __name__ == "__main__":
    start_threaded_tcp_server()
