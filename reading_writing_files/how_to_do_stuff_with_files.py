def write_file_stuff(filename):
    """
    An example of how to write to a file.
    :param filename: a filename chosen by the user passed into the function as a parameter
    :return: void
    """
    with open(filename, 'w') as fp:
        for row in range(10):
            for col in range(10):
                fp.write("{},{} ".format(row, col))
            fp.write("\n")


def read_file_stuff(filename):
    """
    An example of how to read a file.
    :param filename: a filename chosen by the user and passed into the function as a parameter
    :return: void
    """
    with open(filename, 'r') as fp:
        for line in fp:
            row = []
            for col in line.split(" "):
                if not col == '\n':
                    row.append(col)
            coords.append(row)

coords = []
file = "bits_and_bobs.txt"  # the name of the file

write_file_stuff(file)
read_file_stuff(file)
