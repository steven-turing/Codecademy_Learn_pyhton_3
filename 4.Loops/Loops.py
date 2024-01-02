# 1.
# LoopsIn programming, this process of using an initialization, repetitions, and an ending condition is called a loop.
# In a loop, we perform a process of iteration (repeating tasks).

# 2.If we only use print(), our program might look like this:
# Write 10 print() statements below!
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")

# 3.For Loops: Introduction
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
    print(game)

for game in sport_games:
    print(game)

# 4.For Loops: Using Range
promise = "I will finish the python loops module!"

for temp in range(5):
    print(promise)

# 5.While Loops: Introduction
# A while loop performs a set of instructions as long as a given condition is true.
# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
    # Loop Body
    # Print if the condition is still true
    print("Loop Iteration - count <= 3 is still true")
    # Print the current value of count
    print("Count is currently " + str(count))
    # Increment count
    count += 1
    print(" ----- ")
print("While Loop ended")

# Your code below:
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")

# 6.While Loops: Lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
    print("I am learning about " + python_topics[index])
    index += 1