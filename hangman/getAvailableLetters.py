def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    allLetters = string.ascii_lowercase
    lettersAvailable = ""
    for letter in allLetters:
        if letter not in lettersGuessed:
            lettersAvailable += letter
    return lettersAvailable
