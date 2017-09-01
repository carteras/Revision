from random import randint


class Visible(object):
    """
    Objects that can be rendered visually
    """

    def __init__(self, symbol):
        self.symbol = symbol
        self.contains = None

    def show(self):
        """
        If this tile contains another object, render that. Otherwise, render the default symbol
        :return:  return the symbol to be rendered.
        """
        if self.contains:
            return self.contains.show()
        return self.symbol


class Traversable(object):
    """
    Objects that are traversable
    """

    def __init__(self, traversable=False):
        self.traversable = traversable

    def is_traversable(self):
        return self.traversable


class Tile(Visible, Traversable):
    """
    Objects that are Tiles are both Visible and Traversable
    """

    def __init__(self, symbol="!"):
        Visible.__init__(self, symbol)
        traversable = False
        if symbol in ".#+":  # if the symbol is . # or + then it is traversable
            traversable = True
        Traversable.__init__(self, traversable)


class Damageable(object):
    """
    Objects that can be damaged can be hit and can die.
    """

    def __init__(self, hp=1):
        self.hp = hp

    def hit(self, dmg):
        if self.hp > 1:
            self.hp -= dmg
        else:
            self.hp = 0

    def is_alive(self):
        if self.hp < 1:
            return False
        return True


class Updatable(object):
    def touch(self, mob):
        raise NotImplementedError()


class Positional(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, x, y):
        self.x = x
        self.y = y


class Mobile(Visible, Damageable, Positional):
    """
    Objects that can move can be moved and can update their position.
    """

    def __init__(self, symbol, x, y, hp):
        self.x = x
        self.y = y
        Visible.__init__(self, symbol)
        Damageable.__init__(self, hp)

    def move(self):
        """
        All mobile objects have this move by default. Player Objects overload this function for custom
        input and output
        :return: the x and y position that the mobile object will move to.
        """
        direction = randint(1, 10)
        x = self.x
        y = self.y
        if direction == 1:
            y -= 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1
        elif direction == 4:
            x += 1
        return x, y


class Tangible(Visible, Updatable, Positional):
    """
    Some objects can be touched by other objects.
    """
    def __init__(self, symbol, x, y):
        Visible.__init__(self, symbol)
        Updatable.__init__(self)
        Positional.__init__(self, x, y)

    def touch(self, mob):
        """
        This method should give the mob that touched it some advantage like more HP or strength
        :param mob:
        :return:
        """
        print(f"{mob} touched me!!!!")




