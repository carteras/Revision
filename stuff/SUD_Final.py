from Revision.stuff.SUD_GameObjects import Tile, Mobile


class Game(object):
    """
    Handles the core logic for the game.
    """

    def __init__(self, map_file="map.txt"):
        """
        Initialises the game, including making the maze from the map_file
        :param map_file:
        """
        self.maze = []
        self.playing = True
        self.mobs = []

        with open(map_file, 'r') as fp:
            for line in fp:
                row = []
                for col in line:
                    if col == '\n':
                        continue
                    elif col == "_":
                        col = Tile(" ")
                    else:
                        col = Tile(col)
                    row.append(col)
                self.maze.append(row)

    def draw_maze(self):
        """
        renders the map from the maze []
        """
        for line in self.maze:
            for col in line:
                print(col.show(), end='')
            print()

    def update(self, mob, new_x=None, new_y=None):
        """
        Updates the map as players move through
        :param mob: the mobile object moving
        :param new_x: the x position the mobile is moving to
        :param new_y: the y position the mobile is moving to
        :return: True if the move was completed
        """
        if not mob.is_alive():  # check to see if the mob is alive
            self.remove_mob(mob)  # if not, remove it
            return False  # this is a failed move

        if not new_x or not new_y:  # if x and y aren't set
            new_x = mob.x  # set x to current x
            new_y = mob.y  # set y to current y

        future_tile = self.maze[new_y][new_x]  # future_tile is more descriptive of what I'm doing
        if not future_tile.is_traversable():  # if future_tile is not traversable fail
            return False

        # if future tile has an object in it, fail
        if future_tile.contains and mob is not future_tile.contains:
            self.fight(mob, future_tile.contains)  # something here is, hit it!
            return False

        if not future_tile:  # I'm not sure why this is here. It's late.
            return False

        current_tile = self.maze[mob.y][mob.x]  # current_tile is more descriptive
        current_tile.contains = None  # I'm moving from this tile, so remove me from it
        future_tile.contains = mob  # I'm moving TOO this tile, so add me to it
        mob.update(new_x, new_y)  # update the mob so it knows where it is.
        return True  # yay, this is a valid move

    def add_mob(self, mob):
        """
        add a mob to the game
        :param mob: the mobile object that is being added
        :return: True for testing purposes
        """
        self.mobs.append(mob)
        self.update(mob)
        return True

    def remove_mob(self, mob):
        """
        Remove a mob from the list of mobs
        :param mob:  the mobile object to be removed
        """
        current_tile = self.maze[mob.y][mob.x]
        current_tile.contains = None
        self.mobs.remove(mob)

    @staticmethod
    def fight(mob1, mob2):
        """
        Mobile object wants to move onto the tile that mobile 2 is on. This causes a fight
        :param mob1: the mobile object that is moving
        :param mob2: the mobile object that is being hit
        """
        print(f'{mob1.show()} hits {mob2.show()} -> {mob2.hp}')
        mob2.hit(1)


class Player(Mobile):
    """
    The player object. It shares properties with all Mobile Objects
    """

    def __init__(self, player_x=6, player_y=5):
        symbol = '@'
        hp = 10
        Mobile.__init__(self, symbol, player_x, player_y, hp)

    def move(self):
        """
        Player objects change the move function as they accept input from the keyboard
        :return: the x and y position that the player has moved to.
        """
        player_input = input("Press ESDF to move or Q to quit")
        x = self.x
        y = self.y
        if player_input == "e":
            y -= 1
        elif player_input == "d":
            y += 1
        elif player_input == 's':
            x -= 1
        elif player_input == 'f':
            x += 1
        return x, y


class Goblin(Mobile):
    """
    An example monster
    """

    def __init__(self, x=6, y=3):
        symbol = "&"
        hp = 3
        Mobile.__init__(self, symbol, x, y, hp)


g = Game()  # creating a new game
g.add_mob(Player())  # add a player to the game
g.add_mob(Goblin())  # adding a monster to the game
while g.playing:  # while the game is playing, play
    g.draw_maze()  # draw the map
    for m in g.mobs:  # for each mobile object in the game
        mob_x, mob_y = m.move()  # move them, and get the new x y position
        g.update(m, mob_x, mob_y)  # update the game with that new position
