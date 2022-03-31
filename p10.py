#create an interactive dictonary using json

import json
import difflib

file=open(" ") # add the path here with .json extension
dictonary=json.load(file)

word=input("Enter the word")

if word in dictonary.keys():
  print(word, ":", dictonary[word])
else:
  similar=difflib.get_close_matches(word,dictonary.keys())
  if (similar)>0:
    similar=similar[0]
    print("Did you mean ",similar[0],"?, yes or no")
    yorn=input()
    if yorn=="yes":
      print(word, ":", dictonary[similar])
    else:
      print("No match found")
  else:
    print("No match found")