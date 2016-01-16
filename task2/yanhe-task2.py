# __author__ = 'Yan'

import glob
import re


def nyt_reader():
    word_dict = {}
    text_files = glob.glob('nyt/*.txt')
    for text_file in text_files:
        cur_file = open(text_file, 'r')
        content = cur_file.readline().rstrip()
        text = re.findall(r'[a-z]', content.lower())
        for word in text:
            freq = word_dict.get(word, 0) + 1
            word_dict[word] = freq
    return word_dict


def message_reader():
    message_dict = {}
    mit_file = open('mit.txt', 'r')
    for line in mit_file:
        text = re.findall(r'[a-z]', line.lower())
        for word in text:
            freq = message_dict.get(word, 0) + 1
            message_dict[word] = freq
    return message_dict


def char_mapping(text_dict, message_dict):
    mapping_dict = {}
    print 'Start decoding the message.\n'
    word_value = text_dict.values()
    word_list = sorted(word_value)
    message_value = message_dict.values()
    message_list = sorted(message_value)
    for i in xrange(26):
        for mword, mfreq in message_dict.items():
            if mfreq == message_list[i] and mword not in mapping_dict:
                for tword, tfreq in text_dict.items():
                    if tfreq == word_list[i]:
                        mapping_dict[mword] = tword
    # manual refine needed
    mapping_dict['n'] = 's'
    mapping_dict['p'] = 'n'
    mapping_dict['r'] = 'm'
    mapping_dict['m'] = 'f'
    mapping_dict['w'] = 'u'
    mapping_dict['c'] = 'i'
    mapping_dict['e'] = 'c'
    mapping_dict['o'] = 'd'
    mapping_dict['z'] = 'l'
    mapping_dict['x'] = 'g'
    mapping_dict['h'] = 'j'
    mapping_dict['l'] = 'p'
    mapping_dict['q'] = 'x'
    mapping_dict['u'] = 'q'
    mapping_dict['g'] = 'z'
    # add uppercase char into mapping
    for mword, tword in mapping_dict.items():
        mapping_dict[chr(ord(mword) - 32)] = chr(ord(tword) - 32)
    return mapping_dict


def decoder():
    text_dict = nyt_reader()
    message_dict = message_reader()
    mapping = char_mapping(text_dict, message_dict)
    mit_file = open('mit.txt', 'r')
    f = open('yanhe-mit-modified.txt', 'w')
    for line in mit_file:
        for i in xrange(len(line)):
            if line[i] in mapping:
                line = line[0: i] + mapping[line[i]] + line[i + 1: len(line)]
        f.write(line)
    f.close()


if __name__ == "__main__":
    decoder()
