file = 'words.txt'
words = []
with open(file, 'r') as fp:
    for line in fp:
        if line == '\n':
            continue
        words.append(line)

with open(file, 'w') as fp:
    fp.writelines(words)
