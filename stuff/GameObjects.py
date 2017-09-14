class Drawable:
    def draw(self): pass


class Tile(Drawable):
    def __init__(self, symbol, walkable=False):
        self.symbol = symbol
        self.contains = None
        self.walkable = walkable

    def draw(self):
        if self.contains:
            return self.contains.draw()
        return self.symbol

    def is_walkable(self):
        return self.walkable


class Door(Tile):
    def __init__(self, symbol):
        self.OPEN = 0
        self.CLOSED = 1
        self.LOCKED = 2
        self.state = self.get_state(symbol)
        super().__init__(symbol)

    def get_state(self, symbol):
        if symbol == '+':
            return self.CLOSED
        elif symbol == "[":
            return self.LOCKED
        elif symbol == '/':
            return self.OPEN

    def open_door(self):
        if self.state == self.CLOSED:
            self.state = self.OPEN

    def is_walkable(self):
        if self.symbol == '/':
            return True
        return False


class GameFactory(object):
    @staticmethod
    def make_tile(symbol):
        return Tile(symbol)

    @staticmethod
    def make_door(symbol):
        return Door(symbol)


def factory(tile):
    if tile in "+[/":
        return GameFactory().make_door(tile)
    if tile == "_":
        tile = " "
    else:
        tile = "!"
    return GameFactory().make_tile(tile)
