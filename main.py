from classes.hangman import Hangman
from classes.word import Word

def main():

    guesses, lettersGuessed = 8, []
    hangman, word = Hangman(guesses), Word(guesses)

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(hangman.secretWord), ' letters long.'
    print '-------------'

    while hangman.isWordGuessed() == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        hangman.stickman(guesses)
        available = word.getAvailableLetters()
        for letter in available:
            if letter in hangman.lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in hangman.lettersGuessed:
            hangman.lettersGuessed.append(letter)

            guessed = word.countLetter(hangman.secretWord,hangman.lettersGuessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in hangman.secretWord:
            hangman.lettersGuessed.append(letter)

            guessed = word.countLetter(hangman.secretWord,hangman.lettersGuessed)
            print 'Good Guess: ', guessed

        else:
            guesses -= 1
            hangman.lettersGuessed.append(letter)

            guessed = word.countLetter(hangman.secretWord,hangman.lettersGuessed)
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
