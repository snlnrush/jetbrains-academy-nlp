iimport requests
import re
from bs4 import BeautifulSoup


url = 'https://www.nature.com/nature/articles'
params = {'sort': 'Pubdate', 'year': '2020', 'page': '3'}
regexp = r"[\w]+"
saved_articles = []

response = requests.get(url, params=params)
soup = BeautifulSoup(response.content, 'html.parser')
articles = soup.find_all('article')

for article in articles:
    article_parse = article.find('span', {'data-test': 'article.type'})
    article_type = article_parse.text.strip()
    if 'News' == article_type:
        article_title = article.find('a').text.strip().replace("’", '')
        article_title_list = re.findall(regexp, article_title)
        file_name = '_'.join(article_title_list) + '.txt'
        saved_articles.append(file_name)
        article_url = 'https://www.nature.com' + article.find('a').get('href')
        response = requests.get(article_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text_news = bytes(soup.find('div', {'class': 'c-article-body u-clearfix'}).text.strip().replace('\n', ''), encoding='utf-8')
        file = open(file_name, 'wb')
        file.write(text_news)
        file.close()

print(f'Saved articles: {saved_articles}')


"""
Stage 4/5: The Soup is Real
Description
We now have a good deal of knowledge and experience, so let's put it all together and create your first real web scraper. Most of the time, the reason why people create parse-and-scrape programs is to automate the routine tasks of retrieving large data from a website. For example, every machine learning task requires some train data. Let's imagine you're doing research based on the recent science news. For that research, you'll need to have the most recent articles with the type "News" that are posted on the Nature journal website. Each article should be saved to a separate .txt file named after the article's title.

Objectives
Create a program that takes the https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3 URL and then goes over the page source code searching for articles.
Detect the article type and the link to view the article tags and their attributes.
Save the contents of each article of the type "News", that is, the text from the article body without the tags, to a separate file named %article_title%.txt. When saving the file, replace the whitespaces in the name of the article with underscores and remove punctuation marks in the filename (str.maketrans and string.punctuation will be useful for this). Also, strip all trailing whitespaces in the article body and title. For example, the article with the title 'Legendary Arecibo telescope will close forever — scientists are reeling' should be saved to the file named Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt.
(Optional) You may output some result message once the saving is done, but it is not required.
We need to inspect each article to find the tags that represent the article's contents. If you take a closer look at the source code, you will see that every article is enclosed in a pair of <article> tags. Then, each article type is hidden inside a <span> tag containing the data-test attribute with the article.type value. Also, every article includes a link to the article's contents, which is placed inside the <a> tag with the data-track-action="view article" attribute. Once the article page is loaded, save its body wrapped in the <div> tag (look for the word "body" in the class attribute).

Make sure your output file is binary with the UTF-8 character encoding.
Example
This time, the program should not take the URL from the input: hard-code it inside the program. Below is an example of the output:

Saved articles:  ['COVID_research_updates_Immune_responses_to_coronavirus_persist_beyond_6_months.txt', 'What_scientists_really_think_about_the_ethics_of_facial_recognition_research.txt', 'Legendary_Arecibo_telescope_will_close_forever_scientists_are_reeling.txt', 'What_the_data_say_about_asymptomatic_COVID_infections.txt']
The main goal is to save the articles with the correct article bodies once the program has been executed.
"""