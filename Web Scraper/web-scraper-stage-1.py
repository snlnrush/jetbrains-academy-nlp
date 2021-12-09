import requests


url = input('Input the URL:\n')

response = requests.get(url)
MESSAGE_ERROR = 'Invalid quote resource!'

if not response:
    print(MESSAGE_ERROR)
else:
    resp_dict = response.json()
    print(resp_dict.get('content', MESSAGE_ERROR))


"""
Stage 1/5: Wanna Talk to the Internet
Description
We use the Internet everyday. Have you ever wondered how your computer communicates with the Global Web? In this stage, we'll learn how to talk to the Internet from your Python script — and interpret the replies! Your program should send an HTTP request to a URL received from the user input. The user input can be a Quotable resource http://api.quotable.io/quotes/-CzNrWMGIg8V. In this case, the program should print out the Quote extracted from the json body response.

The user input may also contain an invalid URL or a non-existing quote resource, for example, http://api.quotable.io/quotes/1, or a different Quotable page (http://api.quotable.io/authors). Use if-else statements to check the status_code or the json body response to print out the Invalid quote resource! error message when the response code is different from 200, or when there is no quote in the json body response. Your program should ask for input.

You may also need a JSON decoder to solve this task. This will allow you to access particular features such as the content, headers, etc. You can use the json() function from the requests library or the loads() function from the json library. Check out the requests documentation and the json documentation to learn more about them.

Objectives
In this stage, your program should:

Send an HTTP request to a URL received from the user input.
Print out the Quote content extracted from the json body response.
Print out the Invalid quote resource! error message if there's no quote or something goes wrong.
Examples
The greater-than symbol followed by space (> ) represents the user input. Note that it's not part of the input.

Example 1

Input the URL:
> http://api.quotable.io/quotes/-4WQ_JwFWI

The three great essentials to achieve anything worth while are: Hard work, Stick-to-itiveness, and Common sense.
Example 2

Input the URL:
> http://api.quotable.io/quotes/asdfgh
"""
