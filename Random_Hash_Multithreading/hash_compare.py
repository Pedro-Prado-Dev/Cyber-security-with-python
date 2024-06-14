import hashlib

file_1 = 'data/text_1.txt'
file_2 = 'data/text_2.txt'


hash_1 = hashlib.new('ripemd160')
hash_2 = hashlib.new('ripemd160')

hash_1.update(open(file_1, 'rb').read())
hash_2.update(open(file_2, 'rb').read())

if hash_1.digest() != hash_2.digest():
    print(f'File 1: {file_1}  is diferent of File 2: {file_2}')
else:
    print(f'File 1: {file_1}  is equal of File 2: {file_2}\n')
    print(f'{hash_1.digest()}\n')
