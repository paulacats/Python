def decrypt_story():
    myCryptText = get_story_string()
    ciphertext = CiphertextMessage(myCryptText)
    decryptText = ciphertext.decrypt_message()
    return decryptText
