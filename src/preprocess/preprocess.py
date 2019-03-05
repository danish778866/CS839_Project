#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 mohdanishaikh <mohdanishaikh@mohdanishaikh-Inspiron-7573>
#
# Distributed under terms of the MIT license.
import re
import glob
import os

def preprocess_labeled_files(path):
    #files = glob.glob(path)
    #for name in files:
    words = []
    with open(path) as file:
        current_line = file.read()
        current_line = re.sub(r'([,.\"])', r' \1 ', current_line)
        words.extend(current_line.split())
    file.close()
    return words

def is_negative(word):
    ret_val = False
    ignore_punctuations = [",", ".", "\""]
    ignore_words = ["It", "We", "She", "He", "But", "These", "If", "All", "Its", "In", "And", "For", "This", "That", "Or", "On", 
                    "The", "I", "His", "Her", "At", "Then", "There", "Their", "Our", "As", "Was", "How", "What", "Any", "To", "Of",
                   "They", "Have", "Can", "Be", "A", "With", "You", "From", "By", "My"]
    if not word:
        ret_val = True
    elif word[0].islower():
        ret_val = True
    elif re.search(r'\d', word):
        ret_val = True
    elif word in ignore_punctuations:
        ret_val = True
    elif word in ignore_words:
        ret_val = True
    return ret_val

def clean_word(word):
    word = word.replace("\'s", "")
    word = re.sub(r'[^\w\s<>/]', '', word)
    return word

def generate_candidates_labels(words, threshold):
    num_words = len(words)
    gen_threshold = threshold
    is_person = False
    candidates = []
    labels = []
    for i in range(num_words):
        if i + threshold > num_words - 1:
            gen_threshold = num_words - i
        prune = False
        current_word = clean_word(words[i])
        end_person = False
        not_title = True
        if current_word in ["Sir", "Mr", "Ms", "Dr", "Prof", "St"]:
            not_title = False
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
            elif not_title:
                if is_person:
                    labels.append(1)
                else:
                    labels.append(0)
            if not_title:
                candidates.append(current_word)
            
        j = 1
        if is_person:
            local_person = True
        while (j < gen_threshold) and (not prune):
            if is_negative(words[i + j]):
                prune = True
            else:
                current_word = current_word + " " + clean_word(words[i + j])
                if "<person>" in current_word and "</person>" in current_word:
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
    return candidates, labels

def write_data(path, content):
    f = open(path, "w")
    for line in content:
        f.write(str(line) + "\n")
    f.close()

def preprocess_driver(data_dir, candidates_dir, labels_dir):
    files = glob.glob(data_dir)
    words = []
    for name in files:
        words = preprocess_labeled_files(name)  
        file_name = os.path.basename(name)
        candidates_file = candidates_dir + os.sep + file_name 
        labels_file = labels_dir + os.sep + file_name 
        candidates, labels = generate_candidates_labels(words, 4)
        write_data(candidates_file, candidates)
        write_data(labels_file, labels)



#words = []
#candidates = []
#labels = []
path = "/home/mohdanishaikh/Projects/CS839_Project/data/*.txt"
candidates_dir = "/home/mohdanishaikh/Projects/CS839_Project/data/candidates"
labels_dir = "/home/mohdanishaikh/Projects/CS839_Project/data/labels"
preprocess_driver(path, candidates_dir, labels_dir)
#preprocess_labeled_files(path, words)
#generate_candidates_labels(words, 4, candidates, labels)
#num_candidates = len(candidates)
#print(words)
#write_data(output_path, "candidates.txt", candidates)
#write_data(output_path, "labels.txt", labels)
