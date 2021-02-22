#!/bin/python3
from random import randint

times = 0
is_adj = False
nouns = "nouns.txt"
adjectives = "adjectives.txt"

def get_amount():
  global times
  try:
    times = int(input("amount: "))
  except:
    print("error: invalid value")
    get_amount()
get_amount()

def get_is_adj():
  global is_adj
  try:
    is_adj = bool(int(input("adjectives [0, 1]: ")))
  except:
    print("error: invalid value")
    get_is_adj()
get_is_adj()

def get_rand_line ( txt ):
    with open(txt) as f:
        lines = f.readlines()
        var = lines[randint(0, len(lines))]
        var = var[:-1]
    return var

print("")
for i in range(0, times):
    word = ""
    word = get_rand_line(nouns)
    if is_adj == True:
        adj = get_rand_line(adjectives)
        word = adj + " " + word
    print ( word )
print("")
