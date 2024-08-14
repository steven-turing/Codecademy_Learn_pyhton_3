# 1.Reading a File
# So, how do we interact with files using Python? We’re going to learn how to read and write different kinds of files
# using code.
# Use with to open the file welcome.txt. Save the file object as text_file.
# Read the contents of text_file and save the results in text_data.
with open('welcome.txt') as text_file:
    text_data = text_file.read()

print(text_data)

# 2.Iterating Through Lines
# When we read a file, we might want to grab the whole document in a single string, like .read() would return. But
# what if we wanted to store each line in a variable? We can use the .readlines() function to read a text file line
# by line instead of having the whole thing.
with open('how_many_lines.txt') as lines_doc:
    for line in lines_doc.readlines():
        print(line)

# 3.Reading a Line
# Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(),
# which will only read a single line at a time. If the entire document is read line by line in this way subsequent
# calls to .readline() will not throw an error but will start returning an empty string ("").

with open('just_the_first.txt') as first_line_doc:
    first_line = first_line_doc.readline()
    second_line = first_line_doc.readline()

print(first_line)
print(second_line)

# 4.Writing a File
# Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is
# 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.
# It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that
# file, erasing whatever its contents were before.

with open('bad_bands.txt', 'w') as bad_bands_doc:
    bad_bands_doc.write('fenghuangchuanqi')

# 5.Appending to a File
# Isn’t there a way to just add a line to a file without completely deleting it? Of course there is! Instead of opening
# the file using the argument 'w' for write-mode, we open it with 'a' for append-mode.

with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.write("Air Buddy\n")

# 6.What's With "with"?
# The with keyword invokes something called a context manager for the file that we’re calling open() on. This context
# manager takes care of opening the file when we call open() and then closing the file after
# we leave the indented block.

# 7.What Is a CSV File?
# CSV stands for Comma-Separated Values and CSV files are usually the way that data from spreadsheet software
# (like Microsoft Excel or Google Sheets) is exported into a portable format.
# Open logger.csv using our standard with syntax, saving the file object in the temporary variable log_csv_file.

with open('logger.csv') as log_csv_file:
    print(log_csv_file.read())

# 8.Reading a CSV File
# In Python we can convert that data into a dictionary using the csv library’s DictReader object.

import csv

with open('cool_csv.csv') as cool_csv_file:
    cool_csv_dict = csv.DictReader(cool_csv_file)
    for row in cool_csv_dict:
        print(row)

# 9.Reading Different Types of CSV Files
# We call all files with a list of different values a CSV file and then use different delimiters
# (like a comma or tab) to indicate where the different values start and stop.

import csv

with open('books.csv') as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter='@')
    isbn_list = []
    for row in books_reader:
        isbn_list.append(row['ISBN'])
    print(isbn_list)
