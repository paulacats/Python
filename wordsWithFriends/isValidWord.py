def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    valid = True
    copy_of_hand = hand.copy()
    #if word in wordList and all letters in hand, return true, else false
    if word not in wordList:
        valid = False
        return valid
    else:
        for char in word:
            if char not in hand:
                valid = False
                return valid
            else:
                copy_of_hand[char] -= 1
                if copy_of_hand[char] < 0:
                    valid = False
                    return valid
    return valid
