#create an interactive dictonary using json

import json
import difflib

file=open("dic.json") # add the path here with .json extension
dictonary=json.load(file)

word=input("Enter the word ")

if word in dictonary.keys():
  print(word, ":", dictonary[word])
else:
  similar=difflib.get_close_matches(word,dictonary.keys())
  if len(similar)>0:
    similar=similar[0]
    print("Did you mean ",similar,"?, yes or no")
    yorn=input()
    if yorn=="yes":
      print(similar, "means ", dictonary[similar])
    else:
      print("No match found")
  else:
    print("No match found")