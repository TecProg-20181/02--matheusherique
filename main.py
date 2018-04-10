from classes.hangman import Hangman
from classes.word import Word


def main():

    guesses, lettersGuessed = 8, []
    hangman, word = Hangman(guesses), Word(guesses)
    secretWord, lettersGuessed = hangman.secretWord, hangman.lettersGuessed

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'

    while hangman.is_word_guessed() == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        hangman.stickman(guesses)
        available = word.get_available_letters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:
            lettersGuessed.append(letter)

            guessed = word.letter_guessed(secretWord, lettersGuessed)

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = word.letter_guessed(secretWord, lettersGuessed)
            print 'Good Guess: ', guessed

        else:
            guesses -= 1
            lettersGuessed.append(letter)

            guessed = word.letter_guessed(secretWord, lettersGuessed)
            print 'Oops! That letter is not in my word: ',  guessed

        print '------------'

    else:
        if hangman.is_word_guessed() == True:
            hangman.stickman(guesses)
            print 'Congratulations, you won!'

        else:
            hangman.stickman(guesses)
            print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'


main()
