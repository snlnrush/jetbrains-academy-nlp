import requests
import json
from bs4 import BeautifulSoup


url = input('Input the URL:\n')
if url == 'https://www.imdb.com/title/tt0068646/':
    url = 'https://web.archive.org/web/20211101044320/https://www.imdb.com/title/tt0068646/'

headers = {'Accept-Language': 'en-US,en;q=0.5'}
MESSAGE_ERROR = 'Page ERROR!'
films_dict = {}

response = requests.get(url, headers=headers)

if not response:
    print(MESSAGE_ERROR)
elif 'title' not in url:
    print('Invalid movie page!')
else:
    soup = BeautifulSoup(response.content, 'html.parser')
    if not soup.find('title') or not soup.find('script', {'type': 'application/ld+json'}):
        print('Invalid movie page!')
    else:
        films_dict['title'] = soup.find('title').text
        json_str = soup.find('script', {'type': 'application/ld+json'}).contents[0]
        films_dict['description'] = json.loads(json_str)['description']
        print(films_dict)


"""
Stage 2/5: The Beautiful Soup Ingredients

Theory
Some Internet pages might get automatically translated according to your computer's settings. Although this might be useful in everyday life, in this project we ask you to output the data in English. To force requests library to return a page in English, you can use headers with Accept-Language parameter set to the value en-US,en;q=0.5:

response = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
Note that the structure of the page might be different in cases when you use this header and when you don't (even if your default language is English).

Description
We know how to send HTTP requests and get responses. In the previous stage, the example URL responded with the json body, this is how the REST resources communicate with a client. We, humans, go to websites to access the Internet. We also have browsers, but sometimes we need to parse the website's content automatically. Parsing is one of the ways to scrape a webpage.

Parsing website data begins with the inspection of the page source code with browser built-in tools. Usually, the desired information can be distinguished by some unique attributes or a set of attributes, for example, a css class name. We need to determine these attributes and then make our parsing tool (in our case, the beautifulsoup library) do the magic for us.

Objectives
Feed your program a link to a movie or a TV series description. This is an example of a correct link: https://www.imdb.com/title/tt0080684/. Note that the link to a movie or a TV series always contains the word 'title' in it.
Inspect the page and find out how the movie's or a series' title and description are stored in the source code.
Download the webpage content, parse it using the beautifulsoup library, and print out the movie's original title and description in a dictionary. For example, you can find the title in the <title> tag. The description can be found in the <meta> tag with the following template: soup.find('meta', {'name':'description'}). You can access the text within the tags via the text and the ['content'] attributes, respectively.
If the received page doesn't have a movie description or is not an IMDb resource, the program should respond with the Invalid movie page! message, just like in the previous stage.

Examples
A user inputs a URL with a movie description to store it in the response dictionary. If the link is not correct or does not contain a movie original title and description, the program responds with an error message.

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input. Each example corresponds to a separate execution.

Example 1

Input the URL:
> https://www.imdb.com/title/tt0080684/

{"title": "Star Wars: Episode V - The Empire Strikes Back", "description": "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy."}
Example 2

Input the URL:
> https://www.imdb.com/name/nm0001191/

Invalid movie page!
Example 3

Input the URL:
> https://www.google.com/

Invalid movie page!
"""
