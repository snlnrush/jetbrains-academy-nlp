import requests
import re
import os
from bs4 import BeautifulSoup


def parse_articles(url, params, type):
    regexp = r"[\w]+"
    saved_articles = []
    folder_name = f"Page_{params['page']}"
    main_dir = os.getcwd()

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')

    os.mkdir(folder_name)
    os.chdir(os.getcwd() + '/' + folder_name)

    for article in articles:
        article_parse = article.find('span', {'data-test': 'article.type'})
        article_type = article_parse.text.strip()
        if type == article_type:
            article_title = article.find('a').text.strip().replace("’", '')
            article_title_list = re.findall(regexp, article_title)
            file_name = '_'.join(article_title_list) + '.txt'
            saved_articles.append(file_name)
            article_url = 'https://www.nature.com' + article.find('a').get('href')
            response = requests.get(article_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            text_news = bytes(soup.find('div', {'class': 'c-article-body u-clearfix'}).text.strip().replace('\n', ''),
                              encoding='utf-8')
            file = open(file_name, 'wb')
            file.write(text_news)
            file.close()
    os.chdir(main_dir)
    return saved_articles


num_pages = int(input())
in_article_type = input()

url = 'https://www.nature.com/nature/articles'
params = {'sort': 'Pubdate', 'year': '2020'}
saved_articles = []

for n_page in range(1, num_pages + 1):
    params['page'] = str(n_page)
    saved_articles.append(parse_articles(url, params, in_article_type))

print(f'Saved articles: {saved_articles}')


"""
Stage 5/5: Soup, Sweet Soup
Description
You've done an amazing job in the previous stage! Remember we mentioned retrieving large data? Let's improve your program by making it parse multiple website pages. To make it even more useful, let's also implement the opportunity to parse several kinds of articles at once.

Objectives
Improve your code so that the function can take two parameters from the user input: the number of pages (an integer) and the type of articles (a string). The integer with the number of pages specifies the number of pages on which the program should look for the articles.
Go back to the https://www.nature.com/nature/articles?sort=PubDate&year=2020 website and find out how to navigate between the pages with the requests module changing the URL.
Create a directory named Page_N (where N is the page number corresponding to the number input by the user) for each page. Search and collect all articles page by page; filter all the articles by the article type and put all the articles that are found on the page with the matched type to the directory Page_N. Mind that when the user enters some number, for example, 4, the program should search all pages up to that number and the respective folders (Folder 1, Folder 2, Folder 3, Folder 4) should be created. Mind also that in articles of different types the content is contained in different tags.
Save the articles to separate *.txt files. Keep the same processing of the titles for the filenames as in the previous stage. You can give users some feedback on completion, but it is not required.
If there's no articles on the page, your program should still create a folder, but in this case the folder would be empty.

Example
The program takes two input values from the user and then continues to process the Nature website data.

The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

> 4
> Nature Briefing
Saved all articles.
The main goal is to save the articles with the correct article bodies once the program has been executed.
"""