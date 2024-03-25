"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """
    >>> wf = WordFinder("/Users/joelpanepinto/Desktop/Springboard/Python/Tasks/python-oo-practice/words.txt")
    235886 words read

    >>> wf.random()
    'autodidact'

    >>> wf.random()
    'curious'
    """

    def __init__(self, path): 
        """Initializing dictionary and reporting items read"""
        file = open(path)
        self.list = self.read_words(file)
        print(f"{len(self.list)} words read")
        file.close()

    def read_words(self, file):
        """Returning words of list, stripped"""
        return [word.strip() for word in file]

    def random(self):
        """Returning random word in list."""
        rand_num = random.random()*len(self.list)
        return self.list[round(rand_num)]

class SpecialWordFinder(WordFinder):
    """
    with the following code, we make sure only words are read and not spaces, symbols, etc.

    >>> wf2 = SpecialWordFinder("/Users/joelpanepinto/Desktop/Springboard/Python/Tasks/python-oo-practice/words_w_symb.txt")
    4 words read

    >>> wf2.random()
    'mango'

    >>> wf2.random()
    'apple'
    """

    def read_words(self, file):
        return [word.strip() for word in file
                if word.strip() and not word.startswith("#")]