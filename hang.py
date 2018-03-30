# -*- coding: utf-8 -*-

import random
import string

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


class Hangman(Word):
    def __init__(self, guesses):
        Word.__init__(self, guesses = guesses)

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
            print "|      😄      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 5:
            print "________      "
            print "|      |      "
            print "|      😅      "
            print "|             "
            print "|             "
            print "|             "
        elif guesses == 4:
            print "________      "
            print "|      |      "
            print "|      😳      "
            print "|      |      "
            print "|             "
            print "|             "
        elif guesses == 3:
            print "________      "
            print "|      |      "
            print "|      😥      "
            print "|     /|      "
            print "|             "
            print "|             "
        elif guesses == 2:
            print "________      "
            print "|      |      "
            print "|      😰      "
            print "|     /|\     "
            print "|             "
            print "|             "
        elif guesses == 1:
            print "________      "
            print "|      |      "
            print "|      😭      "
            print "|     /|\     "
            print "|     /       "
            print "|             "
        else:
            print "________      "
            print "|      |      "
            print "|     \☠️/     "
            print "|      |      "
            print "|     / \     "
            print "|             "

def getGuessedWord():

     guessed = ''


     return guessed

def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def main():

    guesses = 8
    lettersGuessed = []
    hangman = Hangman(guesses)
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(hangman.secretWord), ' letters long.'
    print '-------------'



    while hangman.isWordGuessed() == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        hangman.stickman(guesses)
        available = getAvailableLetters()
        for letter in available:
            if letter in hangman.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in hangman.lettersGuessed:

            guessed = getGuessedWord()
            for letter in hangman.secretWord:
                if letter in hangman.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in hangman.secretWord:
            hangman.lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in hangman.secretWord:
                if letter in hangman.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in hangman.secretWord:
                if letter in hangman.lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'

    else:
        if hangman.isWordGuessed() == True:
            hangman.stickman(guesses)
            print 'Congratulations, you won!'
        else:
            hangman.stickman(guesses)
            print 'Sorry, you ran out of guesses. The word was ', hangman.secretWord, '.'

main()
