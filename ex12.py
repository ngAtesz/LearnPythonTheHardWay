__author__ = 'ngAtesz'

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))

"""
Study Drills:
1. Use 'python -m pydoc raw_input' on Windows
"""

import pydoc
def main():
    pydoc.doc("input")

if __name__ == "__main__":
    main()

