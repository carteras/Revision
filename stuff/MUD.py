from Revision.stuff.GameObjects import factory

maze = []

with open("map.txt", 'r') as map_fp:
    for line in map_fp:
        x = []
        for col in line:
            if col == "\n":
                continue
            col = factory(col)
            x.append(col)
        maze.append(x)


def draw_maze(maze):
    for y in maze:
        for x in y:
            print(x.draw(), end="")
        print()


draw_maze(maze)
