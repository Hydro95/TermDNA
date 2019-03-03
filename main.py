import sys
from termcolor import colored
from random import randint

if (len(sys.argv) > 1):
    dna_length = int(sys.argv[1])
else:
    dna_length = 20

cols = ['red', 'green', 'yellow', 'blue']
text = ['T', 'A', 'C', 'G']

def genBorders(length):
    str1 = ''
    for i in range(0, length):
        str1 += '='
    return str1

def genStr(length):
    str2 = ''
    for i in range(0, length):
        num = randint(0, len(cols) - 1)
        str2 += colored(text[num], cols[num])
    return str2

def attach(dna):
    str2 = ''
    for i in range(0, len(dna)):
        if (dna[i] == text[0]):
            str2 += colored(text[1], cols[1])
        elif (dna[i] == text[1]):
            str2 += colored(text[0], cols[0])
        elif (dna[i] == text[2]):
            str2 += colored(text[3], cols[3])
        elif (dna[i] == text[3]):
            str2 += colored(text[2], cols[2])

    return str2

str1 = genBorders(dna_length)
sequenced = genStr(len(str1))
print(str1)
print(sequenced)
print(attach(sequenced))
print(str1)
