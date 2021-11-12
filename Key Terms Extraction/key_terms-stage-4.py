from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from lxml import etree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from operator import itemgetter
import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')


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
        temp_list.append(lemmatizer.lemmatize(word))
    return temp_list


def pos_text(list_tokens, type_speech='NN'):
    pos_speech = [nltk.pos_tag([word]) for word in list_tokens]
    temp_list = [word[0][0] for word in pos_speech if word[0][1] == type_speech]
    return temp_list


path_xml = 'news.xml'

xml_root = etree.parse(path_xml).getroot()

data_text = []

head_news = []

for item in xml_root[0]:
    head_news.append(item[0].text)
    text_news = item[1].text
    pre_text_news = [sent.strip() for sent in text_news.split('\n')]
    pre_text_news_2 = rid(lemmatizer_wordnet(word_tokenize(' '.join(pre_text_news).lower())))
    pre_text_news_3 = pos_text(pre_text_news_2, 'NN')
    data_text.append(' '.join(pre_text_news_3))

tfidf_vectorizer = TfidfVectorizer(input='content', encoding='utf-8', use_idf=True,
                                   lowercase=True, analyzer='word', ngram_range=(1, 1),
                                   stop_words=None, vocabulary=None)

tfidf_matrix = tfidf_vectorizer.fit_transform(data_text)

vector_array = tfidf_matrix.toarray()
terms = tfidf_vectorizer.get_feature_names()

most_freq = []

for sent in vector_array:
    nn_freq = []
    for idx, val in enumerate(sent):
        if val > 0:
            nn_freq.append((terms[idx], val))
    most_freq.append([x[0] for x in sorted(nn_freq, key=itemgetter(1, 0), reverse=True)[:5]])

for idx, val in enumerate(head_news):
    print(val + ':')
    print(' '.join(most_freq[idx]), end='\n\n')
