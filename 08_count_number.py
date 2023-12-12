with open(r"00_text_file.txt", 'r') as fp:
    lines = len(fp.readlines())
    print("number of lines is : ", lines)
