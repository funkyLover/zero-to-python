
text = 'Sample text to save. \nNew line.'

save_file = open('file.txt', 'w')

save_file.write(text)
save_file.close()

append_text = '\nappend new line.'

append_file = open('file.txt', 'a')
append_file.write(append_text)
append_file.close()

read_file = open('file.txt', 'r')
file_txt = read_file.read()
print(file_txt)
