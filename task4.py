import os
with open('File_1.txt', 'w') as f:
    f.write("First file text")
with open('File_1.txt') as f:
    first = f.read()


with open('File_2.txt', 'w') as f:
    f.write("Second file text")
with open('File_2.txt') as f:
    second = f.read()


third = first + " " + second
with open('File_3.txt', 'w') as f:
    f.write(third)
with open('File_3.txt') as f:
    print(f.read())


os.remove('File_3.txt')
os.remove('File_1.txt')
os.remove('File_2.txt')