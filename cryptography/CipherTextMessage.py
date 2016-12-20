class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = Message.get_message_text(self)
        self.valid_words = Message.get_valid_words(self)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        goodWords = 0
        highValue = 0
        shift = 0
        goodShiftValue = 0
        cryptedMsg = self.message_text
        myWords = self.valid_words
        bestDecryptMsg = ''
        currentWord = ''
        while shift < 26:
            decrypting_dict = Message.build_shift_dict(self,shift)
            cryptedMsg = Message.apply_shift(self,shift)
            currentWord = cryptedMsg
            cryptedMsg = cryptedMsg.split(' ')
            
            for word in cryptedMsg:
                if word in myWords:
                    goodWords +=1
            
            if goodWords > highValue:
                highValue = goodWords
                #print(highValue)
                goodShiftValue = shift
                #print(goodShiftValue)
                bestDecryptMsg = currentWord
                
            goodWords = 0
            shift +=1
        
        decrypted = (goodShiftValue, bestDecryptMsg)

        return decrypted
