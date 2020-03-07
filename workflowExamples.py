#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:03:38 2019

@author: kaushaldabhi
"""
import re
import string
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from textblob import TextBlob

    
def toLowercase():
    input_str = ”The 5 biggest countries by population in 2017 are China,
    India, United States, Indonesia, and Brazil.”
    
    input_str = input_str.lower()
    
    print(input_str)
    
def removeNumbers():

    input_str = ’Box A contains 3 red and 5 white balls, while Box B contains 4 red and
    2 blue balls’
    result = re.sub(r’\d+’, ‘’, input_str)
    print(result)
    
def removePunct():
        
        
    input_str = “This &is [an] example? {of}
    string. with.? punctuation!!!!” # Sample string
    result = input_str.translate(string.maketrans(“”,””),string.punctuation)
    
    print(result)
    
def tokenization():
        
    text = "God is Great! I won a lottery."
    print(word_tokenize(text))

def stopWord():
        input_str = “NLTK is a leading platform for building Python
    programs to work with human language data.”
    
    stop_words = set(stopwords.words(‘english’))
    
    
    tokens = word_tokenize(input_str)
    
    result = [i for i in tokens if not i in stop_words]
    
    print (result)
    
    
def stemming():
        
        
    stemmer= PorterStemmer()
    
    input_str=”There are several types of stemming
    algorithms.”
    
    input_str=word_tokenize(input_str)
    
    for word in input_str:
    
    print(stemmer.stem(word))
    
    
def speechTagging():
    input_str=”Parts of speech examples: an article, to write, interesting, easily, and, of”
    result = TextBlob(input_str)
    print(result.tags)
    
    
if __name__ == "__main__":
   
    toLowercase()
    removeNumbers()
    tokenization()
    stopWord()
    stemming()
    speechTagging()
    
    