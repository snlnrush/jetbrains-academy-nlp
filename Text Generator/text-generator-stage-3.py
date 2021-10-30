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
