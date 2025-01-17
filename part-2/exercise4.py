import os
import string

dirname = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(dirname, "alice.txt")


def word_frequencies():
    dict = {}
    with open (filename) as text:
        for line in text:
            line = line.lower()
            for char in string.punctuation:
                line = line.replace(char, ' ')
            
            words_array = line.split(" ")
            for word in words_array:
                dict[word] = dict.get(word, 0) + 1
    return dict
print(word_frequencies())
