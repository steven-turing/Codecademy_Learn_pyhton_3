last_semester_gradebook = [["Politics", 80], ["Latin", 96], ["Dance", 97], ["Architecture", 65]]

# Your code below:
subjects = ["Physics", "Calculus", "Poetry", "History"]

grades = [98, 97, 85, 88]

gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]
print(gradebook)

gradebook.append(["Computer Science", 100])
print(gradebook)

gradebook.append(["Visual Arts", 93])
print(gradebook)

gradebook[-1][1] = 98
print(gradebook)

gradebook[2].remove(85)
# you can use the .append() method to add the "Pass" value to the sublist where your "Poetry" class is located.
gradebook[2].append('Pass')
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
