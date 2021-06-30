import string as s
#TODO decrypt def, break class
class multiplicative:

    def __init__(self):
        self.alphabets = s.ascii_uppercase

    def encrypt(self, message, key):
        # it could work though with a bad key but decryption is impossible
        if not self.verifyGoodKeys(key):
            return "Bad key"

        mess = message.upper()
        finalMess = ""

        for i in mess:
            if i in self.alphabets:
                finalMess += self.alphabets[((ord(i)-65)*key)%26]
            else:
                finalMess += i

        return finalMess

    def verifyGoodKeys(self, key):
        return True if key % 2 != 0 and len(self.alphabets) % key != 0 and key != 1 else False

    def decrypt(self, cipher, key):
        pass

class breakMultiplicative:
    pass

a = multiplicative()
print(a.encrypt("ydztg", 15))