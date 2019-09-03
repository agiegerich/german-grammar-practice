from time import sleep
from random import randrange

er_sie_es = ['er', 'sie', 'es']
past_conjugation = ['ich', 'du', 'er', 'sie', 'es', 'wir', 'ihr', 'Sie']

def rand_elem(l):
    return l[randrange(len(l))]

while True:
    for _ in range(60):
        print()
    print('Third person pronoun: '+rand_elem(er_sie_es))
    print('Perfect past pronoun: '+rand_elem(past_conjugation))
    sleep(15)


