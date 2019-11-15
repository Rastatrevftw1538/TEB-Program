#TEB Assignment Note

import nltk

from flask import Flask, render_template

from nltk.corpus import wordnet

import sys

nltk.download('wordnet')

import io

def main(Input):
    #_file = input("Enter the file path of the text you want to search: ")
    #read = open(_file,'r')
    #real_file = read.read()
    real_file = Input.lower()
    #print(real_file)
    #print(real_file)
    count = 0
    #_word = input("Enter the word you want to search for: ")
    emotion_words = {"happy":0,"excited":0,
    "sad":0,"mad":0}
    new_corp = nltk.WordPunctTokenizer().tokenize(real_file)
    #_pos = nltk.pos_tag(nltk.word_tokenize(_word))
    #print(_pos)
    #thing = nltk.wsd.lesk(lang_,_word)
    #print(thing)
    #print(new_corp)

    for x in new_corp:
        #print(x," word")
        times = 0
        for emo_wrd in emotion_words:
            for _syns in wordnet.synsets(emo_wrd):
                #print(_syns," emoWrds")
                for i in _syns.lemmas():
                    #print(i.name()," Synon")
                    if x == i.name() and times <= 0:
                        #print(x," word_in_sent")
                        #print(i.name()," matched syn")
                        emotion_words[emo_wrd] += 1
                        times += 1
                        break
    pos_num = (emotion_words["happy"]+emotion_words["excited"])
    neg_num = (emotion_words["sad"]+emotion_words["mad"])
    note_thing = "Your text has found "+str(pos_num)+" instances of positivity and "+str(neg_num)+" instances of negativity." 
    if pos_num == 0 and neg_num == 0:
        note_final = note_thing+"\n"+"We were unable to determine the emotion behind your text!"
    elif pos_num <= 0 and neg_num >= 1:
        neg_equation = 100
        note_final = note_thing+"\n"+"Your notes are "+str(neg_equation)+"% percent negative."
    elif neg_num <= 0 and pos_num >= 1:
        pos_equation = 100
        note_final = note_thing+"\n"+"Your notes are "+str(pos_equation)+"% percent positive."
    elif pos_num >= 0 and neg_num >= 0:
        pos_equation = int((pos_num)/((pos_num)+(neg_num))*(100))
        neg_equation = int((neg_num)/((pos_num)+(neg_num))*(100))
        note_thing2 = "Your notes are "+str(pos_equation)+"% percent positive and "+str(neg_equation)+"% percent negative"
        
        note_final = note_thing+"\n"+note_thing2
    return note_final,Input

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])