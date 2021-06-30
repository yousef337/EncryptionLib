#TODO decrypt def, break class
class Hill:

    def encrypt(self, text, key):
        if text == "":
            return ""

        text = text.lower()
        keyM = [[ord(key[0]) - 97, ord(key[1]) - 97], [ord(key[2]) - 97, ord(key[3]) - 97]]
        lst = text
        for x in text:
            if not x.isalpha():
                lst = lst.replace(x, "")

        lst += "z" if len(lst) % 2 != 0 else ""
        textM = []
        encr = ""

        for i in range(0, len(lst), 2):
            textM.append([ord(lst[i]) - 97, ord(lst[i + 1]) - 97])

        for i in textM:
            encr += chr(self.muilt(keyM, i)[0] + 97) + chr(self.muilt(keyM, i)[1] + 97)

        return encr.upper()

    def muilt(self, a, b):
        return [(a[0][0] * b[0] + a[0][1] * b[1]) % 26, (a[1][0] * b[0] + a[1][1] * b[1]) % 26]

    def decrypt(self):
        pass

class breakHill:
    pass