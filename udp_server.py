import socket


def start_udp_server():
    """
    Start a UDP server that listens for incoming requests and echoes back what
    it receives.
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 65432)
    print('Starting up on {} port {}'.format(*server_address))
    server_socket.bind(server_address)   

    while True:
        print('Waiting for a message')
        data, address = server_socket.recvfrom(4096)

        print('Received {} bytes from {}'.format(len(data), address))
        print(data)

        if data:
            sent = server_socket.sendto(data, address)
            print('Sent {} bytes back to {}'.format(sent, address))
                                   


# the lines below are our entrypoint - you can run this script by running
# `python udp_server.py` from the command line.
if __name__ == "__main__":
    start_udp_server()
