# __author__ = 'Yan'
import re
import glob
import sys


def name_reader():
    print 'Read names that need to be eliminated.\n'
    full_names = set()
    name_file = open('names.txt', 'r').read().split('\n')
    for line in name_file:
        full_names.add(line)
    return full_names


def text_processor():
    full_names = name_reader()
    print 'Scan the text files and identify the names on the list.\n'
    text_files = glob.glob('nyt/*.txt')
    for text_file in text_files:
        cur_file = open(text_file, 'r')
        content = cur_file.readline().rstrip()
        # text = re.sub('[\W_]+', ' ', content) # get rid of punctuation and numerical string
        for full_name in full_names:
            appeared = re.search(full_name, content)
            if appeared:
                content = re.sub(full_name, 'John Smith', content)
                print text_file, appeared.end(), '\n'
                position = appeared.end()
                last_name = full_name.split(' ')[1]
                first_part = content[0: position]
                second_part = content[position: len(content)]
                second_part = re.sub(last_name, 'Smith', second_part)
                content = first_part + second_part
        f = open('yanhe-nyt-modified/' + text_file.split('/')[1], 'w')
        f.write(content)
        f.close()
    print 'All listed name eliminated.'

if __name__ == "__main__":
    text_processor()