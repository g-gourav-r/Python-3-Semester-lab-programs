## Design a rock paper scissor game
import random
options=["rock","paper","scissor"]
status=True
while status==True:
  uc=input("Enter your choice : ")
  sc=random.choice(options)
  print(sc)
  if(uc=="stop"):
    status=False
  elif(uc==sc):
    print("The game is tie")
  elif(uc=="rock"):
    if(sc=="paper"):
      print("You lose")
    elif(sc=="scissor"):
      print("You win")
  elif(uc=="paper"):
    if(sc=="scissor"):
      print("You lose")
    elif(sc=="rock"):
      print("You win")
  elif(uc=="scissor"):
    if(sc=="rock"):
      print("You lose")
    elif(sc=="paper"):
      print("You win")
  elif uc not in options:
    print("Invalid input")
  