def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    my_String = ''
    for x in secretWord:
        if x in lettersGuessed:
            my_String += x
        else:
            my_String += '_'
    return my_String
