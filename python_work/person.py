# Person

class Person():
    def __init__(self, name, age, height):
        self.name = name
        self.height = height
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.height} tall.")

    def set_hair(self,hair):
        self.hair = hair

    def get_hair(self):
        print(self.hair)


# jack = Person

# print(jack.name)
# print(jack.age)
# print(jack.height)
# jack.talk()