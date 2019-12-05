# TEB Assignment Note

import os
import io
import re

import nltk

from flask import Flask, render_template

from nltk.corpus import wordnet

import math

import sys

nltk.download('wordnet')


def main(Input):
    regex = re.compile("([\w]*)[\s]([\d\S]{2}|[\d]{1})[\n]")
    root = os.path.dirname(os.path.abspath("AFINN-111.txt"))
    read = open(os.path.join(root, 'Corpus/AFINN-111.txt'), 'r')
    corpusThing = read.read()
    real_file = str(Input.lower())
    nums = []
    final_num = ""
    count = 0
    #_word = input("Enter the word you want to search for: ")
    emotion_words = {}
    # emotion_words = {"happy":0,"excited":0,"good":0,
    # "sad":0,"mad":0,"bad":0}
    new_corp = nltk.WordPunctTokenizer().tokenize(real_file)
    #_pos = nltk.pos_tag(nltk.word_tokenize(_word))
    # print(_pos)
    #thing = nltk.wsd.lesk(lang_,_word)
    # print(thing)
    # print(new_corp)

    for thing in regex.finditer(corpusThing):
        emotion_words[thing.group(1)] = thing.group(2)
    # print(emotion_words)

    for x in new_corp:
        #print(x, " word")
        times = 0
        for emo_wrd in emotion_words:
            for _syns in wordnet.synsets(emo_wrd):
                #print(_syns, " emoWrds")
                for i in _syns.lemmas():
                    #print(i.name(), " Synon")
                    if x == i.name() and times <= 0:
                        #print(x, " word_in_sent")
                        #print(i.name(), " matched syn")
                        nums.append(int(emotion_words[emo_wrd]))
                        times += 1
                        print(nums)
                        break
    # print(nums)
    # print(neg_num)
    length = len(nums)
    equation = sum(nums)
    note_thing = "Your text has a polarity score of " + \
        str(int(equation))+" your average score is "+str(int(equation/length))

    note_final = note_thing  # +"\n"+note_thing2
    # print(note_final)
    return note_final, Input


#main("hello i like some kind of food")
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
