from lxml import etree
from nltk import word_tokenize
from collections import Counter
from operator import itemgetter


path_xml = 'news.xml'

xml_root = etree.parse(path_xml).getroot()

for item in xml_root[0]:
    head_news = item[0].text
    text_news = item[1].text
    tokens_list = word_tokenize(text_news.lower())
    freq_words = Counter(tokens_list).most_common(10)
    freq_words.sort(key=itemgetter(1, 0), reverse=True)
    only_words = [word[0] for word in freq_words[: 5]]
    print(head_news + ':')
    print(' '.join(only_words), end='\n\n')
