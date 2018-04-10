import string
import random
from Tkinter import Tk
from tkFileDialog import askopenfilename

class Input(object):
    """Class with all methods used in input of the game

    Attributes:
        secret_word (obj): It`s an object to Tkinter lib.

    """
    def __init__(self):
        self.root = Tk()

    def __open_file(self):
        self.root.withdraw()
        self.root.update()
        filename = askopenfilename()

        while not filename.endswith('.txt'):
            print"Please use a .txt file!"
            filename = askopenfilename()

        return filename

    def load_words(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print"Loading word list from a text file..."

        filename = self.__open_file()

        infile = open(filename, 'r', 0)
        # line: string
        line = infile.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        print"  ", len(wordlist), "words loaded."
        return random.choice(wordlist)
