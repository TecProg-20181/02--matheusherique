from classes.input import Input

class Word(object):
    """Class with all methods used in words of the game

    Attributes:
        secret_word (str): It`s the secret word that the user has to guess.
        letters_guessed (str): It`s the letter of the word that the user guessed.
        guesses (int): It`s the number of guesses that user has yet.

    """
    def __init__(self, guesses):
        self.secret_word = Input().load_words().lower()
        self.letters_guessed = []
        self.guesses = guesses

    def join_letters(self, secret_word):
        join_letters = ''.join(set(secret_word))
        print"\nThe word has ", len(join_letters), " different letters"

    def is_word_guessed(self):
        for letter in self.secret_word:
            if letter in self.letters_guessed:
                pass
            else:
                return False

        return True

    def letter_guessed(self, secret_word, letters_guessed):
        guessed = self.get_guessed_word()
        for letter in secret_word:
            if letter in letters_guessed:
                guessed += letter
            else:
                guessed += '_ '
        return guessed

    @classmethod
    def get_available_letters(cls):
        import string
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase

        return available

    @classmethod
    def get_guessed_word(cls):

        guessed = ''

        return guessed
