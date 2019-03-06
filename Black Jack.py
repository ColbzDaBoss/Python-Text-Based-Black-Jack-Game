"""
New idea for game mode
Two players or Human vs Ai
The person who has a higher score without going over gets thier score as points which then can be used to win the game either by after a certin time ends the player with the most points wins or set a score limit
Score or time limit
"""
"""
Add Scores.txt Write To. WIP Already Started. Use Check To See If Executing Correctly
"""

import random, time, os, Scores.py
from sys import platform

score=0

def varsReset():
  #Vars
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  '_____________'
  ace=11
  two=2
  three=3
  four=4
  five=5
  six=6
  seven=7
  eight=8
  nine=9
  ten=10
  jack=10
  queen=10
  king=10
  '‾‾‾‾‾‾‾‾‾‾‾‾‾'
  playerTotal=0
  aiTotal=0
  elevenAces=0
  tempAces=0
  ignore=True
  solved=False
  hit=1
  freeze=2
  cards=[ace,ace,ace,ace,two,two,two,two,three,three,three,three,four,four,four,four,five,five,five,five,six,six,six,six,seven,seven,seven,seven,eight,eight,eight,eight,nine,nine,nine,nine,ten,ten,ten,ten,jack,jack,jack,jack,queen,queen,queen,queen,king,king,king,king]
  cardsText=['ace','ace','ace','ace','two','two','two','two','three','three','three','three','four','four','four','four','five','five','five','five','six','six','six','six','seven','seven','seven','seven','eight','eight','eight','eight','nine','nine','nine','nine','ten','ten','ten','ten','jack','jack','jack','jack','queen','queen','queen','queen','king','king','king','king']
  defaultCards=cards
  blackjacks=0
  
  hitCode()


def playAgain(x):
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  if x=='loss':
    file=open("Scores.txt","w") 
    file.write(str(score))
    file.close()
    print("Game over! Your total hit "+str(playerTotal)+". Better luck next time\nDo you want to play again? (y/n)")
    print("Your score has been reset to zero.")
    score=0
    answer=input("")
    if answer=='y' or answer=='Y':
      varsReset()
    if answer=='n' or answer=='N':
      quitgame()
  else:
    print("\nDo you want to play again? (y/n)")
    print("Your current score is "+str(score)+"! Keep playing to get more points")
    answer=input("")
    if answer=='y' or answer=='Y':
      varsReset()
    if answer=='n' or answer=='N':
      quitgame()


def quitgame():
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  print("Your score is "+str(score)+"!\nPress enter to quit the game.")
  PrintScore()

def hitCode():
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  randomCard=random.randint(0,len(cards))
  print("\n\n\nDrawing...\nYou got a "+str(cardsText[randomCard]))
  playerTotal+=cards[randomCard]
  if cardsText[randomCard]=='ace':
    elevenAces+=1
  del cards[randomCard]
  del cardsText[randomCard]
  if playerTotal>21:
    for loop in range(elevenAces):
      playerTotal-=ten
      tempAces-=1
      if playerTotal>21:
        ignore=True
      else:
        break
  elevenAces=tempAces
  if playerTotal>21:
    playAgain('loss')
  elif playerTotal==21:
    print("Your total is "+str(playerTotal)+".\nYou Win!!!!!")
    blackjacks+=1
    score+=21
    playAgain('y')
  else:
    tempAces=elevenAces
    hitOrFreeze()


def hitOrFreeze():
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  print("Your total is "+str(playerTotal)+".\nEnter the number corrosponding to your choice of the following: Would you like to 1 hit, or 2 freeze?")
  answer=int(input(""))
  while solved==False:
    if answer==hit or answer==freeze:
      solved=True
    elif answer!=hit or answer!=freeze:
      print("Enter a valid number. 1 for hit, 2 for freeze")
      answer=input("")
  if answer==hit:
    hitCode()
  elif answer==freeze:
    score+=playerTotal
    randomCard=random.randint(0,len(cards))
    futurePlayerTotal=playerTotal+randomCard
    if futurePlayerTotal>21:
      print("Your total is "+str(playerTotal)+".\nIf you hit the next card it would of been a "+str(randomCard)+" and therefor you would of lost, so good choice!!!")
      playAgain('y')
    elif futurePlayerTotal<21:
      print("Your total is "+str(playerTotal)+".\nIf you hit the next card would of been a "+str(randomCard)+" and therefor you would of been able to continue... oh well")
      playAgain('y')
    elif futurePlayerTotal==21:
      print("Your total is "+str(playerTotal)+".\nIf you hit the next card would of been a "+str(randomCard)+" and therefor you would of had a black jack!!!!! That was a major fail.....")
      playAgain('y')
    


def clearScreen():
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  if platform == "linux" or platform == "linux2" or platform == "darwin":
      # linux
      # OS X
      os.system('clear')
  elif platform == "win32":
      # Windows...
      os.system('cls')



def PrintScore():
  global ace,one,two,three,four,five,six,seven,eight,nine,ten,jack,queen,king,playerTotal,aiTotal,elevenAces,tempAces,ignore,cards,cardsText,randomCard,defaultCards,solved,hit,freeze,blackjacks,score
  File=open("Scores.py","w")
  numLines=1
  for line in File:
      numLines+=1
  printScoreText=""+str(numLines)+"="+str(HighScore)
  file.write(str(printScoreText))
  HighScore=
  for loop in range(numLines):

  print("Highscore is currently: "+str(HighScore))
  file.close()
  pause=input("")
  quit()

varsReset()
