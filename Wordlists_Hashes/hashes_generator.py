import hashlib

string = input('Input your text: ')
menu = int(input(''' 
CHOOSE HASH TYPE
1) MD5
2) SHA1
3) SHA256
4) SHA512
             '''))

match menu:
    case 1:
        result = hashlib.md5(string.encode('utf-8'))
        print(result.hexdigest())
    case 2:
        result = hashlib.sha1(string.encode('utf-8'))
        print(result.hexdigest())
    case 3:
        result = hashlib.sha256(string.encode('utf-8'))
        print(result.hexdigest())
    case 4:
        result = hashlib.sha512(string.encode('utf-8'))
        print(result.hexdigest())
    case _:
        print("Invalid menu option")