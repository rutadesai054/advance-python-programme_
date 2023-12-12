def read_file(file_name, nline):
    from itertools import islice
    with open(file_name) as f:
        for line in islice(f, nline):
            print(line)


read_file('00_text_file', 2)
