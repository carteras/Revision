with open("stuff.txt", 'r') as fp:
    for line in fp:
        line = line.strip("\n")
        line = line.split(" ")
        if line[0] == 'SetSoldierStat':
            name = f' "{line[-2]} {line[-1]}" 1'
            line = line[:-2]
            line.append(name)
        print(' '.join(line))

