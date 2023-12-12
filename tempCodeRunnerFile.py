def read_file(file_name,nline):
    from itertools import isslice
    with open(file_name) as f:
        for line in isslice(f,nline):
            print(line)
read_file('00_text_file',2)