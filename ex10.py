__author__ = 'ngAtesz'
# http://learnpythonthehardway.org/book/ex10.html

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


def funny_code():
    """Start a funny endless loop to print out some characters."""
    while True:
        for i in ["/", "-", "|", "\\", "|"]:
            print("%s\r" % i),

if __name__ == "__main__":
    funny_code()
