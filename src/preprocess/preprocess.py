#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 mohdanishaikh <mohdanishaikh@mohdanishaikh-Inspiron-7573>
#
# Distributed under terms of the MIT license.
import re

def preprocess_labeled_files(path, words):
    with open(path) as file:
        current_line = file.read()
        current_line = re.sub(r'([,.\"\'])', r' \1 ', current_line)
        words.extend(current_line.split())
    file.close()

def is_negative(word):
    ret_val = False
    ignore_words = [",", ".", "\"", "\'"]
    if word[0].islower():
        ret_val = True
    elif word[0].isdigit():
        ret_val = True
    elif word == "The":
        ret_val = True
    elif word == "I":
        ret_val = True
    elif word in ignore_words:
        ret_val = True
    return ret_val

def generate_candidates_labels(words, threshold, candidates, labels):
    num_words = len(words)
    gen_threshold = threshold
    is_person = False
    for i in range(num_words):
        if i + threshold > num_words - 1:
            gen_threshold = num_words - i
        prune = False
        current_word = words[i]
        end_person = False
        if is_negative(current_word):
            prune = True
        else:
            if current_word.startswith("<person>") and current_word.endswith("</person>"):
                current_word = current_word.replace("<person>", "").replace("</person>", "")
                labels.append(1)
            elif current_word.startswith("<person>"):
                current_word = current_word.replace("<person>", "")
                is_person = True
                labels.append(1)
            elif current_word.endswith("</person>"):
                current_word = current_word.replace("</person>", "")
                is_person = False
                labels.append(1)
            else:
                if current_word.startswith("Haas"):
                    print("BOOO(" + current_word + ")")
                labels.append(0)
            candidates.append(current_word)
            
        j = 1
        #print("Going for..." + words[i])
        if is_person:
            local_person = True
        while (j < gen_threshold) and (not prune):
            if is_negative(words[i + j]):
                prune = True
            else:
                current_word = current_word + " " + words[i + j]
                if "<person>" in current_word and "</peprson>" in current_word:
                    current_word = current_word.replace("<person>", "").replace("</person>", "")
                elif "<person>" in current_word:
                    current_word = current_word.replace("<person>", "")
                elif "</person>" in current_word:
                    current_word = current_word.replace("</person>", "")
                    end_person = True
                if is_person and local_person:
                    labels.append(1)
                    if end_person:
                        local_person = False
                else:
                    labels.append(0)
                candidates.append(current_word)
                j = j + 1


words = []
candidates = []
labels = []
preprocess_labeled_files("/home/mohdanishaikh/Projects/CS839_Project/data/s_511.txt", words)
generate_candidates_labels(words, 4, candidates, labels)
num_candidates = len(candidates)
for i in range(num_candidates):
    print(candidates[i] + "-" + str(labels[i]))
print(candidates)
print(labels)
print(words)
