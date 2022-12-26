import string
import sys
import nltk

# c = 0
for line in sys.stdin:
    # print(line)
    # c += 1
    for sentence in nltk.sent_tokenize(line):
        # Strip punctuation, word_tokenize, lower-case
        words = [w.strip(string.punctuation).lower() for w in nltk.word_tokenize(sentence)]
        # print(' '.join(nltk.word_tokenize(sentence)).lower().strip(string.punctuation))
        print(' '.join(words))
    # if c > 10:
    #     break