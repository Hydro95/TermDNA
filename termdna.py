import sys
from random import choice
from termcolor import colored

DNA_LENGTH = 20

if len(sys.argv) > 1:
    DNA_LENGTH = int(sys.argv[1])

CHAR_MAP = {
    'T': {'color': 'red', 'links': 'A'},
    'A': {'color': 'green', 'links': 'T'},
    'C': {'color': 'yellow', 'links': 'G'},
    'G': {'color': 'blue', 'links': 'C'}
}


def ch_colored(chara):
    return colored(chara, CHAR_MAP[chara]['color'])


def ch_link(chara):
    return CHAR_MAP[chara]['links']


def gen_dna(length, mid=''):

    top = ''
    bot = ''
    chars = list(CHAR_MAP.keys())

    for _ in range(length):
        rand_ch = choice(chars)
        top += ch_colored(rand_ch)
        bot += ch_colored(ch_link(rand_ch))

    return ''.join('{0}\n{1}\n{2}'.format(top, mid * length, bot))


def main():
    print(gen_dna(DNA_LENGTH, mid='|'))


main()
