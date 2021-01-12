import os
import sys


def isolateBraces(input_file):
    file_in = os.path.join(sys.path[0], input_file + ".txt")
    file = open(file_in, "r")

    text = file.read()

    braces = ''

    for character in text:
        if character in ['(', ')', '[', ']', '{', '}']:
            braces += character

    file.close()

    return braces


def bracesCheck(braces):
    stack = []
    for brace in braces:
        if brace in ['(', '[', '{']:
            stack.append(brace)
        else:
            if not stack:
                print("Braces are not balanced.\n")
                exit()
            last_brace = stack.pop()
            if last_brace == '(':
                if brace != ')':
                    print("Braces are not balanced.\n")
                    exit()
            if last_brace == '[':
                if brace != ']':
                    print("Braces are not balanced.\n")
                    exit()
            if last_brace == '{':
                if brace != '}':
                    print("Braces are not balanced.\n")
                    exit()
    if not stack:
        print("Braces are balanced.\n")
    else:
        print("Braces are not balanced.\n")


def main():
    print("Please, type the name of input file.\n")
    file_name = input()
    isolated_braces = isolateBraces(file_name)
    bracesCheck(isolated_braces)


main()
