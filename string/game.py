import sys
import random
from enum import Enum

class RPS(Enum):  # Use Enum directly
    rock = 1
    paper = 2
    scissors = 3
    
print("")
playerchoice = input("Enter...\n 1 For rock,\n 2 for scisscor,\n 3 for paper:\n\n")
#print(playerchoice)
#print(type(playerchoice))
player = int(playerchoice)
#print(type(player))
if player<1 or player>3:
    sys.exit("please enter b/w 1 or 2 or 3")
computerchoice = random.choice("123")
computer= int(computerchoice)
print("")
print("your choice is " + str(RPS(player)).replace('RPS.',' '))
print("python choice is " + str(RPS(computer)).replace('RPS.',' '))
if (player == computer):
    print("Match Draw😒")
elif(player == 1 and computer == 2):
   print("you Win 🎊🎉🎊🎉🎊🎉")
elif(player ==2 and computer == 3):
    print("you Win 🎊🎉🎊🎉🎊🎉")
elif(player ==3 and computer == 1):
    print("you Win 🎊🎉🎊🎉🎊🎉")
else:
    print("python wins")


