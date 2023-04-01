# Shreya B Deshpande  
# This project is done through Codecademy
# In this project, user answers to an input of their name. A question is asked to the user whether they are ready
# to play the game. Then, a random number is generated from 1 to 9, which gives specific answer for that number.
# Lastly, name with question and following number with answer is printed

import random

name = input("What is your name? ")
question = "Are you ready to play the game?"
answer = ""

random_number = random.randint(1, 9)
print(random_number)

if (random_number == 1):
  answer = ("Yes - definitely")
elif (random_number == 2):
  answer = ("It is decidely so")
elif (random_number == 3):
  answer = ("Without a doubt")
elif (random_number == 4):
  answer = ("Reply hazy, try again")
elif (random_number == 5):
  answer = ("Ask again later")
elif (random_number == 6):
  answer = ("Better not tell you now")
elif (random_number == 7):
  answer = ("My sources say no")
elif (random_number == 8):
  answer = ("Outlook not so good")
elif (random_number == 9):
  answer = ("Very doubtful")
else:
  answer = ("Error")

print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)