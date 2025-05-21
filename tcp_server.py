import socket


def start_tcp_server():
    """
    Start a TCP server that listens for incoming requests and echoes back what
    it receives.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 65432)
    print('Starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)

    server_socket.listen(1)

    while True:
        print('Waiting for a connection')
        connection, client_address = server_socket.accept()
        try:
            print('Connection from', client_address)

            while True:
                data = connection.recv(16)
                print('Received {!r}'.format(data))
                if data:
                    print('Sending data back to the client')
                    connection.sendall(data)
                else:
                    print('No more data from', client_address)
                    break
        finally:
            connection.close()



# the lines below are our entrypoint - you can run this script by running
# `python tcp_server.py` from the command line.
if __name__ == "__main__":
    start_tcp_server()
