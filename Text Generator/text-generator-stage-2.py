from nltk.tokenize import regexp_tokenize

corpus = input()
# corpus = 'corpus.txt'
token_list = []

file = open(corpus, 'r', encoding='utf-8')

template = '[\S]+'

for row in file:
    token_list.extend(regexp_tokenize(row, template))

file.close()

bigram_list = [(token_list[idx], token_list[idx + 1]) for idx in range(len(token_list) - 1)]

print(f'Number of bigrams: ', len(bigram_list))

# print('Corpus statistics')
# print(f'All tokens: {len(token_list)}')
# print(f'Unique tokens: {len(set(token_list))}')

while True:
    idx_token = input()
    if idx_token == 'exit':
        break
    elif idx_token.isalpha():
        print('Type Error. Please input an integer.')
        continue
    elif int(idx_token) >= len(token_list):
        print('Index Error. Please input a value that is in not greater than number of all bigrams.')
        continue
    elif int(idx_token) < 0:
        print('Head: the Tail: North!')
        continue
    elif -1 < int(idx_token) < len(token_list):
        print(f'Head: {bigram_list[int(idx_token)][0]} Tail: {bigram_list[int(idx_token)][1]}')
        continue
