__author__ = 'ngAtesz'

my_name = "Attila Molnar"
my_age = 26
my_height = 172
my_weight = 92
my_eyes = "Green"
my_teeth = "White"
my_hair = "Brown"

print("Let's talk about %s.") % my_name
print("He's %d cm tall.") % my_height
print("He's %d pounds heavy.") % my_weight
print("Actually that is not too heavy")
print("He's got %s eyes and %s hair.") % (my_eyes, my_hair)
print("His teeth are usally %s depending on the coffee.") % my_teeth

# this line is tricky try to get it exactly right
print("If I add %d, %d, and %d I get %d.") % (my_age, my_height, my_weight, my_age + my_height + my_weight)