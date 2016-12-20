def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    isValid = True
    # Keep track of the total score
    score = 0
    totalScore = 0
    # As long as there are still letters left in the hand:
    while sum(hand.values()) > 0:
        # Display the hand
        print("Current hand: ", end="")
        displayHand(hand)
        # Ask user for input
        word = input("Enter a word, or a \".\" to indicate you are finished: ")
        # If the input is a single period:
        if word == '.':
            print("Goodbye! Total score: " + str(totalScore)+ " points.")
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            isValid = isValidWord(word, hand, wordList)
            if not isValid:
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")
                print()
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                size = len(word)
                score = getWordScore(word, size)
                #if the size of the hand is not the size of the word, total -50
                if size != n:
                    score -=50
                totalScore +=score
                print("\" " + word + " \"" + " earned " + str(score)+ " ponts. Total: "+str(totalScore)+" points")
                print()
                # Update the hand 
                hand = updateHand(hand, word)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word != ".":
        print("Run out of letters. Total score: " + str(totalScore)+ " points.")
