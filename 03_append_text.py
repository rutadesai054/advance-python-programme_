from itertools import islice


def file_read(file_name):
    with open(file_name, "w")as file:
        file.write("advance python programme\n")
        file.write("java programme")
        text = open(file_name)
        print(text.read())


file_read('00_text_file.txt')
