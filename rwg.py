#!/bin/python3
import random

times = int(input("how many words? "))
isadj = bool(int(input("should have adjectives? ")))

nouns = "nouns.txt"
adjectives = "adjectives.txt"

def get_rand_line ( txt ):
    with open(txt) as f:
        lines = f.readlines()
        var = lines[random.randint(0, len(lines))]
        var = var[:-1]
    return var

print()
for i in range(0, times):
    word = ""
    word = get_rand_line(nouns)
    if isadj == True:
        adj = get_rand_line(adjectives)
        word = adj + " " + word
    print ( word )
print()

