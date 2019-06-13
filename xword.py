#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "Eileen"

# YOUR HELPER FUNCTION GOES HERE

import re


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    regex_word = test_word.replace(' ', '\\w')
    result = [
        word for word in words if len(test_word) == len(word) and re.match(regex_word, word)
    ]
    print(result)

    # YOUR ADDITIONAL CODE HERE
    raise NotImplementedError('Please complete this')


if __name__ == '__main__':
    main()