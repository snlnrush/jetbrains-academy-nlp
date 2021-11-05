from nltk import word_tokenize
from lxml import etree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from operator import itemgetter
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')


def rid(list_tokens):
    temp_list = []
    for word in list_tokens:
        if word not in string.punctuation and word not in stopwords.words('english'):
            temp_list.append(word)
    return temp_list


def lemmatizer_wordnet(list_tokens):
    lemmatizer = WordNetLemmatizer()
    temp_list = []
    for word in list_tokens:
        temp_list.append(lemmatizer.lemmatize(word, pos='n'))
    return temp_list


path_xml = 'news.xml'

xml_root = etree.parse(path_xml).getroot()

for item in xml_root[0]:
    head_news = item[0].text
    text_news = item[1].text
    tokens_list = rid(lemmatizer_wordnet(word_tokenize(text_news.lower())))
    freq_words = Counter(tokens_list).most_common(10)
    freq_words.sort(key=itemgetter(1, 0), reverse=True)
    only_words = [word[0] for word in freq_words[: 5]]
    print(head_news + ':')
    print(' '.join(only_words), end='\n\n')
