# task2
from re import search
import json

with open('/home/raissov/Desktop/lab5 files/dict.json', 'r') as f:
    data = json.load(f)

print(type(data))

word = str(input("Write some word please:  "))

print("Description of %s" % word)
for i in range(len(data[word])):
    print("%s. %s" % (i + 1, data[word][i]))

print("Some suggestions for you: ")
for i in range(len(data.keys())):
    some_word = list(data)
    if str(some_word[i]).startswith(word):
        print(some_word[i])


