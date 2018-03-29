# -*- coding: utf-8 -*-

import random
import string

WORDLIST_FILENAME = "palavras.txt"


class Word():
    def __init__(self, secretWord, lettersGuessed):
        self.secretWord = secretWord
        self.lettersGuessed = lettersGuessed

    def isWordGuessed(Word):
        secretLetters = []
        lettersGuessed = []

        for letter in secretWord:
            if letter in lettersGuessed:
                pass
            else:
                return False

        return True


class Hangman():
    def stickman(self, guesses):

        if guesses == 8:
			print "________      "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
			print "|             "
        elif guesses == 7:
            print "________      "
            print "|      |      "
            print "|             "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 6:
            print "________      "
            print "|      |      "
            print "|      ˜      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|      |      "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|      "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      õ      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|     \õ/     "
            print "|      |      "
            print "|     / \     "
            print "|             "


def loadWords():
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




def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def main(secretWord):

    guesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    hangman = Hangman()
    word = Word(secretWord, lettersGuessed)

    while word.isWordGuessed() == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        hangman.stickman(guesses)
        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if word.isWordGuessed() == True:
            hangman.stickman(guesses)
            print 'Congratulations, you won!'
        else:
            hangman.stickman(guesses)
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'




secretWord = loadWords().lower()
main(secretWord)
