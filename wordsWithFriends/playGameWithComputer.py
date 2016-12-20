def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    userChoice = ""
    playerChoice = ""
    handsPlayed = 0
    sameHand={}
    
    while userChoice != "e":
        userChoice = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        userChoice = userChoice.lower()
        if userChoice != "e" and userChoice != "n" and userChoice != "r":
            print("Invalid command.")
        if userChoice == "n":
            handsPlayed +=1
            playerChoice = input("Enter u to have yourself play, c to have the computer play: ")
            playerChoice = playerChoice.lower()
            while playerChoice != "u" and playerChoice != "c":
                print("Invalid command.")
                playerChoice = input("Enter u to have yourself play, c to have the computer play: ")
                playerChoice = playerChoice.lower()
            hand = dealHand(HAND_SIZE)
            sameHand = hand
            if playerChoice == "u":
                playHand(hand, wordList, HAND_SIZE)
            else:
                compPlayHand(hand, wordList, HAND_SIZE)
        if userChoice =="r":
            if handsPlayed == 0:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playerChoice = input("Enter u to have yourself play, c to have the computer play: ")
                playerChoice = playerChoice.lower()
                while playerChoice != "u" and playerChoice != "c":
                    print("Invalid command.")
                    playerChoice = input("Enter u to have yourself play, c to have the computer play: ")
                    playerChoice = playerChoice.lower()
                if playerChoice == "u":
                    playHand(sameHand, wordList, HAND_SIZE)
                else:
                    compPlayHand(sameHand, wordList, HAND_SIZE)
        if userChoice =="e":
            break
