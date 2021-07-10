import CH1.GenerlizedJuliusCaesar as gl
import CH1.Multiplicative as mc

class affine:

    def encrypt(self, message, key1, key2):
        encrypted = mc.multiplicative.encrypt(message, key1)
        return gl.additiveCipher.additive(encrypted, key2)

    def decrypt(self, message, key1, key2):
        encrypted = mc.multiplicative.decrypt(message, key1)
        return gl.additiveCipher.additive(encrypted, key2, encrypted = -1)

class breakAffine:

    def breakCipher(self, cipher):
        return gl.breakCipher.breakCipher(mc.breakMultiplicative.breakCipher(cipher))