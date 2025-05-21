import socket


def start_udp_client():
    """
    Start a UDP client that connects to the echo server, then sends a message
    and prints out the response from the server.
    """

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 65432)
    message = b'This is the message. It will be repeated.'

    try:
        print('Sending {!r}'.format(message))
        sent = client_socket.sendto(message, server_address)

        print('Waiting for a response')
        data, server = client_socket.recvfrom(4096)
        print('Received {!r}'.format(data))

    finally:
        print('Closing socket')
        client_socket.close()



# the lines below are our entrypoint - you can run this script by running
# `python udp_client.py` from the command line.
if __name__ == "__main__":
    start_udp_client()
