#The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
#Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

import random
name = "steven"
question = 'Should  I go on vacation next week?'
answer = ""

random_number = random.randint(1,10)
#print(random_number)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number ==2:
  answer = "It is decidedly so"
elif random_number ==3:
   answer ="Without a doubt"
elif random_number ==4:
   answer ="Reply hazy, try again"
elif random_number ==5:
   answer ="Ask again later"
elif random_number ==6:
   answer ="Better not tell you now"
elif random_number ==7:
   answer ="My sources say no"
elif random_number ==8:
   answer ="Outlook not so good"
elif random_number ==9:
   answer ="Very doubtful"
elif random_number ==10:
   answer ="Pretty good idea"
else:
  answer ="Error"

if name == "" or question == "":
  if name == "":
      print("Please tell me  your name.")
  else:
      print("Please provide a question")
else:
      print(name + " asks: " + question)
      print("Magic 8-Ball's answer: " + answer)
