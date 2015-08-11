__author__ = 'ngAtesz'
# http://learnpythonthehardway.org/book/ex12.html

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))

"""
Study Drills:
1. Use 'python -m pydoc raw_input' on Windows
Or just create a batch file with:
    @pythonFolder @pythonFolder\Lib\pydoc.py %*
    and create a environment variable named "pydoc" so we can use it from command line
"""

import pydoc
def main():
    pydoc.doc("input")

if __name__ == "__main__":
    main()

