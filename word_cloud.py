#!/usr/bin/env python3

import wordcloud
import os

def remove_special_char(sentences):
    '''This function removes any special characters like comma, period, exclamation mark, etc.'''
    new_sentence=''
    for letter in sentences:
        if letter.isalpha() or letter==' ':
            new_sentence+=letter
    return new_sentence

def word_frequency(sentences,common_words):
    '''This function creates a dictionary with words as it's key and their respective frequency in the sentence as it's value, excluding the list of common words.'''
    frequency={}
    words=sentences.split()
    for word in words:
        if word not in common_words:
            if word not in frequency:
                frequency[word]=0
            frequency[word]+=1
    return frequency

def creatingWordCloud(frequency):
    '''Creating a WordCloud image with the given words passed as keys in the frequency dictionary.'''
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequency)
    cloud.to_file("myWordCloud.jpg")


sentence=''
file=open(os.getcwd()+"\wordcloud.txt",mode='r',encoding='UTF-8')  #opening file 'wordcloud.txt' and reading it's contents in sentence
for lines in file.readlines():
    sentence=sentence+lines
file.close()                #closing file 'wordcloud.txt'

sentence=remove_special_char(sentence) #receiving the whole sentence without any punctuation mark or special characters
frequency=word_frequency(sentence,common_words=["a", "an","for","that", "to", "if","and","is","the","he","she","i","of","are"]) #receiving a dictionary with word frequencies
creatingWordCloud(frequency)