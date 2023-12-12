from collections import counter


def word_count(file_name):
    with open(file_name) as f:
        return counter(f.read().split())


print("number of word in the file : ", word_count('00_text_file.txt'))
