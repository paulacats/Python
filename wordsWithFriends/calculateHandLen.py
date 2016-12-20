def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLength = 0
    for item in hand.values():
        handLength += item
    return handLength
