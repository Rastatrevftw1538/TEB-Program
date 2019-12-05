# TEB Assignment Note

import os
import io
import re

import nltk

from flask import Flask, render_template

from nltk.corpus import wordnet

import sys

nltk.download('wordnet')


def main(Input):
    regex = re.compile("([\w]*)[\s]([\d\S]{2}|[\d]{1})[\n]")
    root = os.path.dirname(os.path.abspath("AFINN-111.txt"))
    read = open(os.path.join(root, 'app/Corpus/AFINN-111.txt'), 'r')
    corpusThing = read.read()
    real_file = str(Input.lower())
    pos_num = 0
    neg_num = 0
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
    #print(new_corp)

    for thing in regex.finditer(corpusThing):
        emotion_words[thing.group(1)] = thing.group(2)
    #print(emotion_words)

    for x in new_corp:
        #print(x," word")
        times = 0
        for emo_wrd in emotion_words:
            for _syns in wordnet.synsets(emo_wrd):
                #print(_syns," emoWrds")
                for i in _syns.lemmas():
                    #print(i.name()," Synon")
                    if x == i.name() and times <= 0:
                        #print(x, " word_in_sent")
                        #print(i.name(), " matched syn")
                        check = float(emotion_words[emo_wrd])
                        if check > 0:
                            pos_num += int(emotion_words[emo_wrd])
                        elif check < 0:
                            neg_num += int(emotion_words[emo_wrd])
                        times += 1
                        break
    #print(pos_num)
    #print(neg_num)
    total_polar = pos_num+neg_num
    note_thing = "Your text has a polarity score of "+str(total_polar)
    # if total_polar == 0:
    #note_final = note_thing+"\n"+"We were unable to determine the emotion behind your text!"
    # elif total_polar <= 0:
    #neg_equation = 100
    #note_final = note_thing+"\n"+"Your notes are "+str(neg_equation)+"% percent negative."
    # elif neg_num <= 0 and pos_num >= 1:
    #pos_equation = 100
    #note_final = note_thing+"\n"+"Your notes are "+str(pos_equation)+"% percent positive."
    # elif pos_num >= 0 and neg_num >= 0:
    #pos_equation = int((pos_num)/((pos_num)+(neg_num))*(100))
    #neg_equation = int((neg_num)/((pos_num)+(neg_num))*(100))
    #note_thing2 = "Your notes are "+str(pos_equation)+"% percent positive and "+str(neg_equation)+"% percent negative"

    note_final = note_thing  # +"\n"+note_thing2
    #print(note_final)
    return note_final, Input


#main("hello i like some kind of food")
if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])
