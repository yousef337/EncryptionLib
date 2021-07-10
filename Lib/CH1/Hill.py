import numpy as np
#TODO fix some issues -> Update it using only numpy
class Hill:

    def encrypt(self, text, key):
        if text == "":
            return ""

        text = text.upper()
        keyM = [[ord(key[0]) - 65, ord(key[1]) - 65], [ord(key[2]) - 65, ord(key[3]) - 65]]
        lst = text
        for x in text:
            if not x.isalpha():
                lst = lst.replace(x, "")

        lst += "Z" if len(lst) % 2 != 0 else ""
        textM = []
        encr = ""

        for i in range(0, len(lst), 2):
            textM.append([ord(lst[i]) - 65, ord(lst[i + 1]) - 65])

        for i in textM:
            encr += chr(self.muilt(keyM, i)[0] + 65) + chr(self.muilt(keyM, i)[1] + 65)

        return encr.upper()

    def muilt(self, a, b):
        return [(a[0][0] * b[0] + a[0][1] * b[1]) % 26, (a[1][0] * b[0] + a[1][1] * b[1]) % 26]

    def matrixInverse(self, matrix):
        det = matrix[0] * matrix[3] - matrix[1] * matrix[2]
        inverse = det*[matrix[3], -matrix[1], -matrix[2], matrix[0]]
        return inverse

    def decrypt(self, text, key):
        return self.encrypt(text, self.matrixInverse(key))

class breakHill:

    def breakCipher(self, cipher):
        # Using only the most 2 common digraphs in English
        mostCommonEng = ["TH", "HE"]
        mostCommonEngMatrix = [[ord(mostCommonEng[0][0]) - 65, ord(mostCommonEng[0][1]) - 65], [ord(mostCommonEng[1][0]) - 65, ord(mostCommonEng[1][1]) - 65]]
        mostCommonMessMatrix = self.getHighestDigraphs(cipher.upper())
        mostCommonEngMatrixInverse = [[mostCommonEngMatrix[1][1]%26,(-mostCommonEngMatrix[0][1])%26],[(-mostCommonEngMatrix[1][0])%26,mostCommonEngMatrix[0][0]%26]]

        print(mostCommonEngMatrixInverse)
        print(mostCommonMessMatrix)
        key = np.dot(mostCommonMessMatrix,mostCommonEngMatrixInverse)%26
        print(key)
        hill = Hill()
        keyChain = [key[0][0],key[0][1],key[1][0],key[1][1]]
        return hill.decrypt(cipher, keyChain) # will give an exception, fix this


    def getHighestDigraphs(self, cipher):
        cipherLst = cipher.split()
        digraphsFreq = {}

        for a in cipherLst:
            if a not in digraphsFreq.keys():
                digraphsFreq[a] = 0

            digraphsFreq[a] += 1

        highest = []

        for i in range(2):
            for item in digraphsFreq:
                if digraphsFreq[item] == max(digraphsFreq.values()) and len(highest) <= i and item not in highest:
                    highest.append(item)
                    digraphsFreq[item] = 0

        return np.array([[ord(highest[0][0])-65,ord(highest[1][0])-65],[ord(highest[0][1])-65,ord(highest[1][1])-65]])


