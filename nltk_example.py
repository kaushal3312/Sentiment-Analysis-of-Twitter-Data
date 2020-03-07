#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 02:41:01 2019

@author: kaushaldabhi
"""

import nltk
import nltk.sentiment.sentiment_analyzer 

# Analysing for single words
def OneWord(): 
    positive_words = ['good', 'progress', 'luck']
    text = 'A great mans greatest good luck is to die at the right time'.split()               
    analysis = nltk.sentiment.util.extract_unigram_feats(text, positive_words) 
    print('\n ****** Sentiment with one word ******\n')
    print(analysis) 
    
# Analysing for a pair of words	
def WithBigrams(): 
    word_sets = [('Regular', 'increase'), ('increase', 'decrease')] 
    text = 'Daily hard work leads to regular increase in different aspect of our lives”'.split() 
    analysis = nltk.sentiment.util.extract_bigram_feats(text, word_sets) 
    print('\n***** Sentiment with bigrams *****\n') 
    print(analysis)
    
# Analysing the negation words. 
def NegativeWord():
    text = 'The coffee shop is not yet open for another batch of service crew.'.split() 
    analysis = nltk.sentiment.util.mark_negation(text) 
    print('\n****** Sentiment with Negative words ******\n')
    print(analysis) 
    
if __name__== "__main__":
    
    OneWord()
    WithBigrams() 
    NegativeWord() 