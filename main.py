# Create a program to introduce your robot using OOPs concepts.
""" Harsh has two Robots - Tom and Jerry, which he bought from you, but those robots have some internal problems they cannot
introduce their names. So help harsh in making his robots introduce their names using Classes and Objects, as you have
desianed those robots. """

class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")

t = Robot("Tom")
j = Robot("Jerry")

t.introduce()
j.introduce()