#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 mohdanishaikh <mohdanishaikh@mohdanishaikh-Inspiron-7573>
#
# Distributed under terms of the MIT license.


def preprocess_labeled_files(path, words):
    with open(path) as file:
        current_line = file.read()
        words.extend(current_line.split())
    file.close()

def generate_candidates_labels(words):
    num_words = len(words)
    for i in range(num_words):
        print(words[i])

words = []
preprocess_labeled_files("/home/mohdanishaikh/Projects/CS839_Project/data/511.txt", words)
generate_candidates_labels(words)
