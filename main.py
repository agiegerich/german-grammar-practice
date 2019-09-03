from random import randrange

words = [1, 2, 3]

print (words[randrange(len(words))])

print('Hello world')

class Noun:
    def __init__(self, english, gender, german, german_plural):
        self.definite_article = gender
        self.english = english
        self.german = german
        self.german_plural = german_plural


def handle_noun(noun_data):
    return noun;

def

with open('word_files/wordbank.csv', 'r') as f:
    line_number = 1
    nouns = []
    for line in f:
        separated = line.strip().split(',')
        word_type = separated[0];
        if word_type == 'noun':
            noun = Noun(noun_data[2], noun_data[3], noun_data[4], noun_data[5])
            nouns.append(noun)
        elif word_type == 'verb':
            verb = Verb
        line_number += 1

    for noun in nouns:
        print(noun.gender_article)


