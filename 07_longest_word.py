def longest_word(file_name):
    with open(file_name, 'r') as infile:
        words = infile.read().split()
    max_length = len(max(words, key=len))
    return [word for word in words if len(word) == max_length]


print(longest_word('00_text_file.txt'))
