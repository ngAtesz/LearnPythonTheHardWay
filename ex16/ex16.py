__author__ = 'ngAtesz'
# http://learnpythonthehardway.org/book/ex16.html

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that hit CTRL-C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three line.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("And finally, we close it.")
target.close()
