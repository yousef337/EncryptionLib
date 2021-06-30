import string as s
#TODO break class
class additiveCipher:

    def additive(self, message, key, encrypt = 1):
        """
        :param message: the intended message
        :param key: an integer of addition
        :param encrypt: 1 for encryption, -1 for decryption
        :return: the (en)/(de)crypted message
        """
        alphabets = s.ascii_uppercase
        mess = message.upper()
        finalMess = ""

        for i in mess:
            if i in alphabets:
                finalMess += alphabets[((ord(i)-65) + encrypt *key)%26]
            else:
                finalMess += i

        return finalMess

class breakCipher:
    pass
