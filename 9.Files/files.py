with open('welcome.txt') as text_file:
    text_data = text_file.read()

print(text_data)

# When we read a file, we might want to grab the whole document in a single string, like .read() would return. But
# what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line
# by line instead of having the whole thing.
with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(),
# which will only read a single line at a time. If the entire document is read line by line in this way subsequent
# calls to .readline() will not throw an error but will start returning an empty string ("").

with open('just_the_first.txt') as first_line_doc:
    first_line = first_line_doc.readline()
    second_line = first_line_doc.readline()

print(first_line)
print(second_line)

# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is
# 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

with open('bad_bands.txt','w') as bad_bands_doc:
  bad_bands_doc.write('fenghuangchuanqi')
