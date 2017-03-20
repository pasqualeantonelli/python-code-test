import __future__
from sys import argv

# Pass a script name and name of file as an argument
script, filename = argv

# TXT is equal to the content of the filename information
txt = open(filename)

# Enter the script name and filename
print("Here's your file %r:" % filename)

# Print the lines of the txt file
print txt.read()

# Let's do the same thing again!
#Enter the two arguments again
print("Type the filename again:")

# File_Again is equal to the passed arguments
file_again = raw_input(">")

# TXT_AGAIN is opened to the file's data content
txt_again = open(filename)

# The data is printed to stdout
print txt_again.read()
