__author__ = 'ngAtesz'
# http://learnpythonthehardway.org/book/ex11.html

print("How old are you?"),
age = input()
print("How tall are you?"),
height = input()
print("How do you weight?"),
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (
    age, height, weight))
