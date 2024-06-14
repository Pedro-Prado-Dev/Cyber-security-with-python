import itertools

string = input('Input your word: ')
result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))