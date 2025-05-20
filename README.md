# networking

Learning the basics of networking with Python.

## Aims

1. Implement the TCP server within the `tcp_server.py` file.
2. Implement the TCP client within the `tcp_client.py` file.
3. Implement the UDP server within the `udp_server.py` file.
4. Implement the UDP client within the `udp_client.py` file.

## Supporting documentation

https://medium.com/@AlexanderObregon/python-for-network-programming-a-beginners-overview-e9379cc44479

Use the above article to implement the clients and servers. Don't worry about
the threading parts of that article, just do the simple version of each.

## Further work

1. Try using the `telnet` command to connect to the TCP echo server with the
   command `telnet localhost port` where you replace `port` with the port your
   server is configured to listen on.
2. Try using the `telnet` command to connect to the UDP echo server. What
   happens and do you know why?
3. Update the server so that you can configure the port on which it listens. You
   can do this by using the python `input()` function within the entrypoint to
   your script and then pass the received port as a parameter to the
   `start_tcp_server()` or the `start_udp_server()` functions.
