items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('00_text_file.txt', 'w')
for item in items:
    file.write(item+"\n")
file.close()
