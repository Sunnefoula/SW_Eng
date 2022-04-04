def populate_file(filename):
    spring = ['January', 'February', 'March', 'April']
    with open('months.txt', 'w') as output_file:
        for month in spring:
            output_file.write(month)
            output_file.write('\n')


def read_file(filename):
    data = []
    with open('months.txt', 'r') as input_file:
        for line in input_file:
            yield line
            # data.append(line)
    # return data


filename = "spring.txt"
populate_file(filename)
file_contents = read_file(filename)
for file_line in file_contents:
    print(file_line)
