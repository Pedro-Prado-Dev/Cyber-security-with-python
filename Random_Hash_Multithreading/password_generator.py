import random
import string

size = int(input('Input a size of password: '))
chars = string.ascii_letters + string.digits + '@!_%$&-+=$' 

rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars) for i in range(size)))