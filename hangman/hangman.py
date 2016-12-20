def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWord = secretWord
    yourGuess = ''
    numGuesses = 8
    wordGuessed = False
    lettersGuessed = ''
    print("Welcome to the game, Hangman! ")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    while numGuesses > 0:
        print("You have " + str(numGuesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        yourGuess = input("Please guess a letter: ")
        yourGuess = yourGuess.lower()
        if yourGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))	
            print("-----------")
        elif yourGuess in secretWord:
            lettersGuessed +=yourGuess
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            wordGuessed = isWordGuessed(secretWord, lettersGuessed)
            if wordGuessed:
                print("Congratulations, you won.")
                break
        else:
            lettersGuessed +=yourGuess
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            numGuesses -=1
            if numGuesses == 0:
                print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
