import math
import random

# delete unnecessary chars in list
def format_line(list: list) -> str:
    remove_chars = ['[', ']', "'", ',']
    new_list = str(list)

    for char in remove_chars:
        new_list = new_list.replace(char, '')

    return new_list

# generate fruits
def generate_fruit(matrix: list) -> list:
    lineIndex = random.randint(0, len(matrix) -1)
    columnIndex = random.randint(0, len(matrix[0]) -1)

    return [lineIndex, columnIndex]