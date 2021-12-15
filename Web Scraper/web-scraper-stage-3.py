import requests


url = input('Input the URL:\n')

response = requests.get(url)

if not response:
    print(f'\nThe URL returned {response.status_code}!')
else:
    file = open('source.html', 'wb')
    file.write(response.content)
    file.close()
    print('\nContent saved.')


"""
Stage 3/5: What the File
Theory
Apart from writing files in the usual text mode, it is also possible to write files in binary mode. It means that Python won't encode the data while writing it to the file. This can be done by passing the argument "wb" to the open() function instead of the usual "w":

file = open('file.html', 'wb')
To retrieve a page's content while using the requests library, the content attribute can be used:

page_content = requests.get(inp_url).content
Please, use these bits of knowledge in your code for this stage.

Description
In previous stages, we retrieved the results and printed them out on the screen. It's handy for one-time running programs or for debugging, but if we want to reuse the data (and that's the case most of the time), storing it is more effective. The simplest way to store data is to write it to a file on your computer.

In this stage, we are going to store the state of a webpage at the moment when the program is executed. It means that we need to get its source code, the content, and save it to an .html file.

Objectives
Create a program that retrieves the page's source code from a user input URL. Please, don't decode the page's content.
Save the page's content to the source.html file. Please, write the file in binary mode.
Print the Content saved. message if everything is OK (Don't forget to add a check for the status_code).
If something is wrong, print the message The URL returned X, where X is the received error code.
Examples
The program receives a URL to retrieve the data from the user input, saves the data to the source.html file, and responds with the successful completion message. Otherwise, it should notify a user about an error.

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input. Each example corresponds to a separate execution.

Example 1

Input the URL:
> https://www.facebook.com/

Content saved.
Example 2

Input the URL:
> http://google.com/asdfg

The URL returned 404!
"""
