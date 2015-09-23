__author__ = 'Samuel'

tabTest = """Ceci est un test encrypter, on verra bien le resultat"""

def CEASAR_ENCRYPT(tab, key):
    newTab = ""
    tab = tab.upper()
    for i in tab:
        nb = ord(i)
        if nb > 64 and nb < 91:
            nb += key
            if nb > 90:
                nb = 64 + (nb-90)
            newTab += (chr(nb))
    return newTab

def CEASAR_DECRYPT(tab, key):
    newTab = ""
    tab = tab.upper()
    for i in tab:
        nb = ord(i)
        if nb > 64 and nb < 91:
            nb -= key
            if nb < 65:
                nb = 91 - (65 - nb)
            newTab += chr(nb)
    return newTab

def FREQ_ANALYSE(tab):
    newTab = ""

newTab = CEASAR_ENCRYPT(tabTest, 3)
print(newTab)
newTab = CEASAR_DECRYPT(newTab, 3)
print(newTab)