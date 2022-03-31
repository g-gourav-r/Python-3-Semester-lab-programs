# Hangman game

hint ="This fruit keeps doctor away"
word = "apple"
guess=["_"]*len(word)
turns=len(word)+1
print("Hint :", hint)

while turns>0:
  print(guess)
  letter=input("Guess the letter : ")
  if letter in word:
    for index in range(len(word)):
      if letter == word[index]:
        guess[index]=letter
    print('Right guess')
  else:
    print('Wrong guess')
    turns-=1
    print("Reaminfing turns", turns)
  if list(word)==guess:
      print("Guessed the word properly")
      break