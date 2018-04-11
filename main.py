from classes.hangman import Hangman
from classes.word import Word


def main():

    guesses = 8
    hangman, word = Hangman(guesses), Word(guesses)
    secret_word, letters_guessed = hangman.secret_word, hangman.letters_guessed

    print'Welcome to the game, Hangman!'
    print'I am thinking of a word that is', len(secret_word), ' letters long.'
    word.join_letters(secret_word)
    print'-------------'

    while not hangman.is_word_guessed() and guesses > 0:
        print'You have ', guesses, 'guesses left.'
        hangman.stickman(guesses)
        available = word.get_available_letters()
        for letter in available:
            if letter in letters_guessed:
                available = available.replace(letter, '')

        print'Available letters', available
        letter = raw_input("Please guess a letter: ")

        if letter in letters_guessed:
            letters_guessed.append(letter)
            guessed = word.letter_guessed(secret_word, letters_guessed)
            print'Oops! You have already guessed that letter: ', guessed

        elif letter in secret_word:
            letters_guessed.append(letter)
            guessed = word.letter_guessed(secret_word, letters_guessed)
            print'Good Guess: ', guessed

        else:
            guesses -= 1
            letters_guessed.append(letter)
            guessed = word.letter_guessed(secret_word, letters_guessed)
            print"Oops! That letter is not in my word: ", guessed
        print'------------'

    else:
        if hangman.is_word_guessed():
            hangman.stickman(guesses)
            print'Congratulations, you won!'

        else:
            hangman.stickman(guesses)
            print'Sorry, you ran out of guesses. The word was ', secret_word, '.'


main()
