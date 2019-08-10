# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:20:56 2019

@author: study
"""

    # check if the typed word is in the words list
    word_num = len(words)
    for k in range(word_num):
        if inword==words[k]:
            words.pop(k)
            word_num -= 1
            break
