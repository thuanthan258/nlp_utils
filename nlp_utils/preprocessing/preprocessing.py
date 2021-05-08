import nltk
import re

def get_ngrams_count(text: str, n_grams: int, min_freq: int) -> dict:
    """
    Get the frequency distribution for inputed ngrams
    Inputs:
        text: str
            The documen you want to calculate the distribution for
        n_grams: int
            The number of gram you want to tokenize
        min_freq: int
            The minimum frequency you want to keep
    Return
        dict: The frequency distribution of your inputed number of gram
    """
    output = {}
    tokens = nltk.word_tokenize(text)
    
    assert n_grams <= 3, "Only 2 grams and 3 grams are supported"
    
    if n_grams == 2:
        gs = nltk.bigrams(tokens)
    elif n_grams == 3:
        gs = nltk.trigrams(tokens)
        
    fdist = nltk.FreqDist(gs)
    for k, v in fdist.items():
        if v > min_freq:
            index = ' '.join(k)
            output[index] = v
    return output

def remove_special_chars(text: str) -> str:
    """
    Remove unnecessary characters
    Input:
        text: str  
            The text your want to process
    Return:
        str: The text after preprocessed
    """
    compile = re.compile(r' +')
    