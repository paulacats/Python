def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    inWord = False
    for letter in secretWord:
        if letter in lettersGuessed:
            inWord = True
        else:
            inWord = False
            break

    return inWord
    
