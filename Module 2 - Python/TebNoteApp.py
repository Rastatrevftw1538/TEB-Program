#TEB Assignment Note

import nltk

from nltk.corpus import wordnet 

import io

def main():
    _file = input("Enter the file path of the text you want to search: ")
    read = open(_file,'r')
    real_file = read.read()
    print(real_file)
    count = 0
    word_tupile = []
    Sent_list = []
    _word = input("Enter the word you want to search for: ")
    new_corp = nltk.WordPunctTokenizer().tokenize(real_file)
    _syns = wordnet.synsets(_word)
    print(_syns[0].name())
    #_pos = nltk.pos_tag(nltk.word_tokenize(_word))
    #print(_pos)
    #thing = nltk.wsd.lesk(lang_,_word)
    #print(thing)
    print(new_corp)
    for x in new_corp:
        if x == _word:
            count += 1
    print("Your corpus has found",count,"of the word",_word, "and it's synonyms")
main()
