#Importing necessary modules
import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

#Defining a method to tokenize words. Splits a sentence into an array of words (tokens)
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

#Defining a method to stem words. First turn the word into all lower case and then finds the root form of the word
def stem(word):
    return stemmer.stem(word.lower())

#Defining a method to create a bag of words. Returns an array of 1s (if a known word exists in the sentence) or 0s (if it doesn't)
def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
