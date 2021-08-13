import string
import random
    
def id_generator(size, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

n_tokens = 1000 # number of tokens to generate
nchars = 10 # length of the token
tokens = [id_generator(nchars) for i in range(1, n_tokens)]

with open('tokens.txt', 'w') as f:
    for token in tokens:
        f.write("%s\n" % token)