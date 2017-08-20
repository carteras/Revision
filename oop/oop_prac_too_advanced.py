class Move(object):
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return "move {}".format(self.speed)


class Fly(Move):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        return "flap " * self.speed


class Run(Move):
    def __init__(self, speed):
        super().__init__(speed)

    def move(self):
        return "run " * self.speed


class Bird(object):
    def __init__(self, name, age, species, voice, special):
        self.name = name
        self.age = age
        self.species = species
        self.voice = voice
        self.special = special


class FlyingBird(Bird, Fly):
    def __init__(self, name, age, species, voice, special, speed):
        super().__init__(name, age, species, voice, special)
        super(Fly, self).__init__(speed)


class NonFlyingBird(Bird, Run):
    def __init__(self, name, age, species, voice, special, speed):
        super().__init__(name, age, species, voice, special)
        super(Run, self).__init__(speed)


class Parrot(FlyingBird):
    def __init__(self, name, age):
        species = "Parrot"
        voice = "squark"
        special = 'something?'
        speed = 5
        super().__init__(name, age, species, voice, special, speed)

    def move(self):
        out = "{} and goes {}".format(self.name, super().move())
        return out


class Emu(NonFlyingBird):
    def __init__(self, name, age):
        species = 'Emu'
        voice = "booms"
        special = 'looks dodgy'
        speed = 4
        super().__init__(name, age, species, voice, special, speed)

    def move(self):
        return "{} {}'s and goes {}".format(self.name, self.special, super().move())


p = Parrot("Carole", 42)
e = Emu("Ernie", 5)
print(p.move())
print(e.move())
