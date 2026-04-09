# Socket programming is a technique in which we communicate between two nodes connected in a network where the server node listens to the incoming requests from the client nodes.

# What are Sockets?
# Sockets are the endpoints of a bidirectional communications channel.
# Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.
#
# A socket is identified by the combination of IP address and the port number. It should be properly configured at both ends to begin communication.

# Python socket Module
#   socket.socket (socket_family, socket_type, protocol=0)

#   family − AF_INET by default. Other values - AF_INET6 (eight groups of four hexadecimal digits), AF_UNIX, AF_CAN (Controller Area Network) or AF_RDS (Reliable Datagram Sockets).
#   socket_type − should be SOCK_STREAM (the default), SOCK_DGRAM, SOCK_RAW or perhaps one of the other SOCK_ constants.
#   protocol − number is usually zero and may be omitted.

# Server Socket Methods
import socket
server = socket.socket()
server.bind(('localhost',12345))
server.listen()
client, addr = server.accept()
print ("connection request from: " + str(addr))