__author__ = 'ngAtesz'
# http://learnpythonthehardway.org/book/ex18.html

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)


# this one tkaes no arguments
def print_none():
    print("I got nothing.")

print_two("Peter", "Marshall")
print_two_again("Peter", "Marshall")
print_one("Asimov")
print_none()
