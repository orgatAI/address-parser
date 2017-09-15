#!/usr/bin/env python
# -*-coding=utf-8-*-


class PrefixQuery(object):
    def __init__(self, words):
        self.prefix_dict = {}
        self._init(words)

    def _init(self, words):
        for word in words:
            len_w  = len(word)
            for i in range(1, len_w+1):
                w = word[:i]
                if i == len_w:
                    self.prefix_dict[w] = 1
                elif w not in self.prefix_dict:
                    self.prefix_dict[w] = 0

    def query(self, text):
        t_len = len(text)
        result_word = ""
        last_index = -1
        for i in range(t_len):
            for j in range(i+1, t_len+1):
                word = text[i:j]
                if word in self.prefix_dict and self.prefix_dict[word] == 1:
                    if j < t_len and text[i:j+1] not in self.prefix_dict:
                        result_word = word
                        last_index = j - 1
                    elif j == t_len:
                        result_word = word
                        last_index = j - 1
        return result_word, last_index+ 1
