from nltk.tokenize import regexp_tokenize

corpus = input()
# corpus = 'corpus.txt'
token_list = []

file = open(corpus, 'r', encoding='utf-8')

template = '[\S]+'

for row in file:
    token_list.extend(regexp_tokenize(row, template))

print('Corpus statistics')
print(f'All tokens: {len(token_list)}')
print(f'Unique tokens: {len(set(token_list))}')

while True:
    idx_token = input()
    if idx_token == 'exit':
        break
    elif idx_token.isalpha():
        print('Type Error. Please input an integer.')
        continue
    elif int(idx_token) >= len(token_list):
        print('Index Error. Please input an integer that is in the range of the corpus.')
        continue
    elif int(idx_token) < 0:
        print('North!')
        continue
    elif -1 < int(idx_token) < len(token_list):
        print(token_list[int(idx_token)])
        continue
