class Bird(object):
    def __init__(self, name, sex, age, distance, move_style):
        self.name = name
        self.sex = sex
        self.age = age
        self.distance = distance
        self.move_style = move_style

    def move(self):
        move = self.move_style * self.distance
        return "{} goes {} ".format(self.name, move)

class Magpie(Bird):
    def __init__(self, name, sex, age):
        distance = 5
        move_style = "swoop"
        super().__init__(name, sex, age, distance, move_style)



class Parrot(Bird):
    def __init__(self, name, sex, age):
        distance = 5
        move_style = "flap"
        super().__init__(name, sex, age, distance, move_style)


p = Parrot("Charlie", "female", 4)
e = Magpie("Ernie", 'male', 2)

print(p.move())
print(e.move())
