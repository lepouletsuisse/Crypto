__author__ = 'Samuel'

import string
from math import sqrt
alphabet = string.ascii_uppercase

dic_francais = {"A":9.42,"B":1.02, "C":2.64, "D":3.39, "E":15.87, "F":0.95, "G":1.04, "H":0.77, "I":8.41, "J":0.89,
                "K":0.01, "L":5.34, "M":3.24, "N":7.15, "O":5.14, "P":2.86, "Q":1.06, "R":6.46, "S":7.90, "T":7.26,
                "U":6.24, "V":2.15, "W":0.01, "X":0.30, "Y":0.24, "Z":0.32}

tabTest = """L'abbaye a ete fondee en 1146 par Sigurd, eveque de Bergen, sur les terres d'une ferme qu'il
possedait, alors que la christianisation du pays etait presque complete. Les premiers moines sont venus de
l'abbaye de Fountains en Angleterre. Il s'agit de la premiere abbaye cistercienne de Norvege, construite
sur le modele de celles existantes a l'epoque en France et en Angleterre.
Comme c'est la regle de cet ordre, les moines ont fait voeu de pauvrete, renoncant a tous les revenus
sauf ceux de la terre, ils developperent ainsi beaucoup d'habilete dans les cultures. Avec le temps,
cela a mene l'abbaye a acquerir beaucoup d'autres fermes, la rendant toujours plus riche et puissante.
En tout, le monastere possedait 50 fermes a Os et bien plus encore dans la region."""

def cesar_encrypt(tab, key):
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

def cesar_decrypt(tab, key):
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

def freq_analyse(tab):
    tab = tab.upper()
    nbLetter = len(tab)
    dic = {}
    for c in alphabet:
        dic[c] = 0
    for i in tab:
        if ord(i) < 91 and ord(i) > 64:
            dic[i] += 1
    for key, val in dic.items():
        dic[key] = val/nbLetter * 100
    return dic

def print_dic_sort_by_alphaKey(dic):
    for c in alphabet:
        for key, nb in dic.items():
            if key == c:
                print(key + " : " + str(nb))

def get_min_dic(dic, *pos_para, **min_lim):
    minTab = ["", 10000]
    if 'min_lim' in min_lim:
        for key, val in dic.items():
            if val < minTab[1] and val > min_lim['min_lim']:
                minTab[0] = key
                minTab[1] = val
    else:
        for key, val in dic.items():
            if val < minTab[1]:
                minTab[0] = key
                minTab[1] = val
    return minTab

def cesar_general(tab):
    dic_prob = {}
    for i in range(1,26):
        tmpTab = cesar_decrypt(tab, i)
        dic_freq = freq_analyse(tmpTab)
        score = 0
        for alpha, freq in dic_francais.items():
            score += pow(dic_freq.get(alpha) - freq, 2) / freq
        dic_prob[i] = sqrt(score)
    print("Le message recu est le suivant: ")
    print(tab)
    print("Le message cherche a une cle de " + str(get_min_dic(dic_prob)[0]) + " et voici son contenue dechiffrer")
    print(cesar_decrypt(tab, get_min_dic(dic_prob)[0]))


cesar_general(cesar_encrypt(tabTest, 7))