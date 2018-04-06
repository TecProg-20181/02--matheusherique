import string
import random

WORDLIST_FILENAME = "palavras.txt"

class Word(object):
    def __init__(self, guesses):
        self.secretWord = self.loadWords().lower()
        self.lettersGuessed = []
        self.guesses = guesses

    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False

        return True

    def loadWords(self):
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

    def countLetter(self, secretWord, lettersGuessed):
        guessed = self.getGuessedWord()
        for letter in secretWord:
            if letter in lettersGuessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed


    def getAvailableLetters(self):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available

    def getGuessedWord(self):

        guessed = ''

        return guessed
