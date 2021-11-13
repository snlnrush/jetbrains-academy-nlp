import random
from nltk.tokenize import regexp_tokenize
from nltk.util import trigrams
from collections import Counter


def check_start_word():
    while True:
        word = random.choice(list(chain_dict.keys()))
        # print(word)
        if word[0].istitle() and word[0].isalnum():
            return word


def check_end_word(word):
    start_word = word
    while True:
        next_word = random.choices(list(chain_dict[start_word].keys()), list(chain_dict[start_word].values()))[0]
        if next_word[-1] in ('.', '?', '!'):
            return next_word
        start_word = start_word[1], next_word


def gen_sentence(start_word, len_sentence):
    sentence = []
    sentence.append(' '.join(start_word))
    for _ in range(len_sentence - 1):        
        if len(sentence) > 3 and sentence[-1][-1] in ('.', '?', '!'):
            return sentence
        next_word = random.choices(list(chain_dict[start_word].keys()), list(chain_dict[start_word].values()))[0]
        sentence.append(next_word)
        start_word = start_word[1], next_word    
    return sentence


corpus = input()
# corpus = 'corpus.txt'

token_list = []
chain_dict = {}

template = r'[\S]+'

with open(corpus, 'r', encoding='utf-8') as file:
    for line in file:
        token_list.extend(regexp_tokenize(line, template))

bigram_list = [(token_list[idx], token_list[idx + 1]) for idx in range(len(token_list) - 1)]

trigram_list = list(trigrams(token_list))

#file = open('trigrams.txt', 'w', encoding='utf-8')
#for line in trigram_list:
#    file.writelines(' '.join(line) + '\n')
#file.close()

# print(list(trigram_list)[:10])

for head1, head2, tail in trigram_list:
    key = (head1, head2)
    chain_dict.setdefault(key, [])
    chain_dict[key].append(tail)

for key, value in chain_dict.items():
    chain_dict[key] = Counter(value)

final_text = []

count = 0

while count < 10:
    sentence_length = random.randint(5, 10)
    start_word = check_start_word()    
    test_sentence = gen_sentence(start_word, sentence_length)
    if test_sentence[-1][-1] not in ('.', '?', '!'):
        continue
    else:
        final_text.append(test_sentence)
        count += 1

for item in final_text:
    print(' '.join(item))
