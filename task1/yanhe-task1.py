# __author__ = 'yanhe'

import re
import glob


def name_reader():
    # Read names that need to be eliminated.
    full_names = set()
    name_file = open('names.txt', 'r').read().split('\n')
    for line in name_file:
        full_names.add(line)
    return full_names


def text_processor():
    full_names = name_reader()
    # Scan the text files and identify the names on the list.
    text_files = glob.glob('nyt/*.txt')
    for text_file in text_files:
        cur_file = open(text_file, 'r')
        content = cur_file.readline().rstrip()
        for full_name in full_names:
            appeared = re.search(full_name, content)
            # Replace the target name
            if appeared:
                content = re.sub(full_name, 'John Smith', content)
                position = appeared.end()
                last_name = full_name.split(' ')[1]
                first_part = content[0: position]
                second_part = content[position: len(content)]
                # If the full name appears before, eliminate the last name
                second_part = re.sub(last_name, 'Smith', second_part)
                content = first_part + second_part
        # Write the updated content into text file
        f = open('yanhe-nyt-modified/' + text_file.split('/')[1], 'w')
        f.write(content)
        f.close()


if __name__ == "__main__":
    text_processor()
