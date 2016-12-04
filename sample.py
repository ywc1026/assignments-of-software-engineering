# -*- coding: utf-8 -*-
# __author__: Yu

from sys import argv
from string import ascii_lowercase

END_OF_SENTENCE = '.?!'


if __name__ == "__main__":
    # read files
    try:
        doc_file = open(argv[1])
        query_file = open(argv[2])
        doc = doc_file.read()
        query = query_file.read().splitlines()
    finally:
        doc_file.close()
        query_file.close()

    # toLowerCase()
    doc = doc.lower().strip()
    len_of_query = len(query)
    for index in range(len_of_query):
        query[index] = query[index].lower()

    # count
    head, tail, length = 0, 0, len(doc)
    nums_of_sentence, nums_of_words = 1, 0
    words, ans = [], [''] * len_of_query
    while tail < length:
        while tail < length and doc[tail] in ascii_lowercase:
            tail += 1
        if tail < length and head < tail:
            word = doc[head:tail]
            words.append(word)
            nums_of_words += 1
            while tail < length and not doc[tail] in ascii_lowercase:
                if doc[tail] in END_OF_SENTENCE:
                    for index_of_words in range(nums_of_words):
                        for index_of_query in range(len_of_query):
                            if words[index_of_words] == query[index_of_query]:
                                ans[index_of_query] += str(nums_of_sentence) + '/' \
                                                       + str(index_of_words + 1) + ','
                    nums_of_sentence += 1
                    nums_of_words = 0
                    words = []
                    tail += 1
                    break
                tail += 1
            head = tail
        else:
            tail += 1
            head = tail

            # print
        for index_of_query in range(len_of_query):
            if ans[index_of_query] == '':
                print(None)
            else:
                print(ans[index_of_query][:-1])
