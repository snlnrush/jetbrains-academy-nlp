import random
from nltk.tokenize import regexp_tokenize
from collections import Counter


def check_start_word():
    while True:
        word = random.choice(token_list)
        if word.istitle() and word[-1].isalnum():
            return word


def check_end_word(word):
    while True:
        if word[0][-1] in ('.', '?', '!'):
            return word
        start_word = random.choice(token_list)
        word = random.choices(list(chain_dict[start_word].keys()), list(chain_dict[start_word].values()))


def gen_sentence(start_word, len_sentence):
    sentence = []
    for _ in range(len_sentence - 1):
        sentence.append(start_word)
        if len(sentence) >= 5 and sentence[-1][-1] in ('.', '?', '!'):
            return sentence
        next_word = random.choices(list(chain_dict[start_word].keys()), list(chain_dict[start_word].values()))
        start_word = next_word[0]
    sentence.extend(check_end_word(start_word))
    return sentence


corpus = input()
#corpus = 'corpus.txt'

token_list = []
chain_dict = {}

template = r'[\S]+'

with open(corpus, 'r', encoding='utf-8') as file:
    for line in file:
        token_list.extend(regexp_tokenize(line, template))

bigram_list = [(token_list[idx], token_list[idx + 1]) for idx in range(len(token_list) - 1)]

for head, tail in bigram_list:
    chain_dict.setdefault(head, [])
    chain_dict[head].append(tail)

for key, value in chain_dict.items():
    chain_dict[key] = Counter(value)

final_text = []

for _ in range(10):
    sentence_length = random.randint(5, 11)
    start_word = check_start_word()
    final_text.append(gen_sentence(start_word, sentence_length))

#print(final_text)

for item in final_text:
    print(' '.join(item))
