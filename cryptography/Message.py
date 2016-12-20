class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.myShift = shift
        shiftDictionary = {}
        origLowerList = []
        origUpperList = []
        shiftLowerList = []
        shiftUpperList = []
        shiftAllLetters = []
        allLetters = string.ascii_lowercase + string.ascii_uppercase
        allLowerLetters = string.ascii_lowercase
        allUpperLetters = string.ascii_uppercase

        origLowerList = list(allLowerLetters)
        origUpperList = list(allUpperLetters)
        origAllLetters = list(allLetters)

        #make a copy of the original
        shiftLowerList = origLowerList [:]
        shiftUpperList = origUpperList [:]

        assert (0 <= self.myShift < 26)
        
        #remove up to shift value from the front
        for i in range(self.myShift):
            shiftLowerList.pop(0)
            shiftUpperList.pop(0)

        #add the removed items to the back
        for i in range(self.myShift):
            shiftLowerList.append(origLowerList[i])
            shiftUpperList.append(origUpperList[i])

        #combine the lists
        shiftAllLetters = shiftLowerList + shiftUpperList
        shiftDictionary = dict(zip(origAllLetters, shiftAllLetters))
        
        return shiftDictionary
        
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.myShift = shift
        msg = self.get_message_text()
        shiftedMsg = ""
        myDict = self.build_shift_dict(self.myShift)
        for letter in msg:
            if letter in myDict:
                shiftedMsg = shiftedMsg + myDict[letter]
            else:
                shiftedMsg = shiftedMsg + letter
        return shiftedMsg
