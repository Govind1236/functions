
# Reading a file
# f = open('file.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# writing a file
# f = open("FILE1.TXT", 'w')
# text = f.write('Hello world!!')
# f.close()

# appending a file
f = open("FILE1.TXT", 'a')
text = f.write('Hello world!!')
print(text)
f.close()