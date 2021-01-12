import os
import sys


def connectFirstToLastName(input_first_name, input_last_name):
    file_first_name = os.path.join(sys.path[0], input_first_name + ".txt")
    file_first = open(file_first_name, "r")
    file_last_name = os.path.join(sys.path[0], input_last_name + ".txt")
    file_last = open(file_last_name, "r")

    file_output_name = os.path.join(sys.path[0], "meta.txt")
    file_output = open(file_output_name, "w+")

    for line_first in file_first:
        parsed_line_first = line_first.strip().split(" ")
        for line_last in file_last:
            parsed_line_last = line_last.strip().split(" ")
            if parsed_line_first[1] == parsed_line_last[1]:
                file_output.write(
                    parsed_line_first[0] + ' ' + parsed_line_last[0] + ' ' + parsed_line_first[1] + '\n')
        file_last.seek(0)

    file_first.close()
    file_last.close()
    file_output.close()


def sort(output):
    file_meta_name = os.path.join(sys.path[0], "meta.txt")
    file_meta = open(file_meta_name, "r")

    file_output_name = os.path.join(sys.path[0], output + ".txt")
    file_output = open(file_output_name, "w+")

    ids = []

    i = 0

    for line in file_meta:
        parsed_line = line.strip().split(" ")
        ids.insert(i, parsed_line[2])
        i += 1

    ids.sort()

    file_meta.seek(0)
    for id in ids:
        for line in file_meta:
            parsed_line = line.strip().split(" ")
            if id == parsed_line[2]:
                file_output.write(line)
        file_meta.seek(0)

    file_meta.close()
    file_output.close()

    os.remove(os.path.join(sys.path[0], "meta.txt"))


def main():
    print("Please, type the name of input file containing first names and IDs.\n")
    first_in = input()
    print("Please, type the name of input file containing last names and IDs.\n")
    last_in = input()
    print("Please, type the name of output file.\n")
    output = input()

    connectFirstToLastName(first_in, last_in)

    sort(output)

    print("Processing of files finished.\n")


main()
