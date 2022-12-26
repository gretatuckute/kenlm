import string
import sys
import nltk

# c = 0
for line in sys.stdin:
    # print(line)
    # c += 1
    for sentence in nltk.sent_tokenize(line):
        # Strip punctuation, word_tokenize, lower-case
        words = [w.strip(string.punctuation).lower() for w in nltk.wordpunct_tokenize(sentence)]
        words_joined = " ".join(words)
        # Get rid of several spaces
        words_joined = " ".join(words_joined.split())
        print(words_joined)
    # if c > 30:
    #     break