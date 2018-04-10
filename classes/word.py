import string
import random

WORDLIST_FILENAME = "palavras.txt"


class Word(object):
    def __init__(self, guesses):
        self.secretWord = self.__load_words().lower()
        self.lettersGuessed = []
        self.guesses = guesses

    def is_word_guessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def __load_words(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print "Loading word list from file..."
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r', 0)
        # line: string
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = string.split(line)
        print "  ", len(wordlist), "words loaded."
        return random.choice(wordlist)

    def letter_guessed(self, secretWord, lettersGuessed):
        guessed = self.get_guessed_word()
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    def get_available_letters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available

    def get_guessed_word(self):

        guessed = ''

        return guessed
