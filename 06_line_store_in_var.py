def read_file(file_name):
    with open(file_name, "r") as myfile:
        a = myfile.readline()
        print(a)


read_file('00_text_file.txt')
