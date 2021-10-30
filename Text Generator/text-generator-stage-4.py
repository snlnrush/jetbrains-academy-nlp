import random
from nltk.tokenize import regexp_tokenize
from collections import Counter

corpus = input()
# corpus = 'corpus.txt'

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

start_word = random.choice(token_list)
# start_word = 'so'
# print(start_word)
# print(chain_dict[start_word])
# print(chain_dict[start_word].keys())
# print(chain_dict[start_word].values())
next_word = random.choices(list(chain_dict[start_word].keys()), list(chain_dict[start_word].values()))
# print(next_word[0])
sentence = []

for _ in range(100):
    sentence.append(start_word)
    next_word = random.choices(list(chain_dict[start_word].keys()), list(chain_dict[start_word].values()))
    start_word = next_word[0]

for idx in range(0, 100, 10):
    print(' '.join(sentence[idx: idx + 10]))

# print(sentence)

"""
while True:
    in_head = input()
    if in_head == 'exit':
        break
    try:
        print(f'Head: {in_head}')
        for key, value in chain_dict[in_head].most_common():
            print(f'Tail: {key}'.ljust(14), f'Count: {value}')
    except KeyError:
        print('Key Error. The requested word is not in the model. Please input another word.')
"""
