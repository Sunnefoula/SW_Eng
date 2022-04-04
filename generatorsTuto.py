import os


def populate_file(filename):
    values_to_write = ["hi", "hello", "geia"]
    with open(filename, 'w') as out:
        for value in values_to_write:
            out.write(value)
            out.write('\n')


def read_file(filename):
    data=[]
    with open(filename, 'r') as in_file:
        for line in in_file:
            #yield line
            data.append(line)
    return data


def read_if_exists(filename):
    if os.path.isfile(filename):
        yield from read_file(filename)
    return []


filename = "another_file.txt"

populate_file(filename)
file_contents = read_file(filename)
print(file_contents)

# generator expression
#file_contents = read_if_exists(filename)

#for file_line in file_contents:
    #print(file_line)
