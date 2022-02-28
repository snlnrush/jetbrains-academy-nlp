import argparse
import socket
import sys


def socket_interaction(**kwargs):
    with socket.socket() as client_socket:
        hostname = kwargs['ip']
        port = int(kwargs['port'])
        message = kwargs['m']
        address = (hostname, port)
        client_socket.connect(address)
        data = message.encode()
        client_socket.send(data)
        response = client_socket.recv(1024)
        response = response.decode()
        print(response)

# parser = argparse.ArgumentParser(description='Stage 1/5: Establishing a connection')
# parser.add_argument('-i', '--ip', default='127.0.0.1', help='Hostname or hosts IP')
# parser.add_argument('-p', '--port', default='9090', help='Number of port')
# parser.add_argument('-m', '--message', default='test', help='Message')
# args = parser.parse_args()
# print(args)
# param = {'ip': args.ip, 'port': args.port, 'm': args.message}


param = {'ip': sys.argv[1], 'port': sys.argv[2], 'm': sys.argv[3]}

socket_interaction(**param)

"""
Stage 1/5: Establishing a connection

Description

Imagine some admin who runs a website on the Internet. The site is becoming very popular, and a lot of people register. Filling in their profiles, they leave some information there that is not meant to be public, for example, information about their credit cards.

The admin completely forgot about the security of the site, so now you can log in with admin privileges without even having a login and password!

The first task of this project is to go to the admin's site; it will immediately give out all the secret information. Remember, as soon as you enter the site as an admin, you will automatically obtain all the private data of the site. It will get harder: the tasks of all other stages of the project will be to crack the admin password. Good luck!

Your program should connect to the server using an IP address and a port from the command line arguments. You can use socket module to create this program.

Objectives
Your program will receive command line arguments in this order:

IP address
port
message for sending
The algorithm is the following:

Create a new socket.
Connect to a host and a port using the socket.
Send a message from the third command line argument to the host using the socket.
Receive the server�s response.
Print the server�s response.
Close the socket.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> python hack.py localhost 9090 password
Wrong password!
Example 2:

> python hack.py 127.0.0.1 9090 qwerty
Connection Success!
"""