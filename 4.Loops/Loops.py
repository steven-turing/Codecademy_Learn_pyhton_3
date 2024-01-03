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

# 7.Infinite Loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
    # students_period_A.append(student)
    print(student)

# 8.Loop Control: Break
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

# 9.Loop Control: Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
    if age < 21:
        continue
    print(age)

# 10.Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    for data in location:
        scoops_sold += data

print(scoops_sold)
