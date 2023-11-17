import os

def statistic(file):

    letters_count = 0
    words_count = 0
    lines_count = 0

    with open(file, 'r') as f:
        for line in f:
            letters_count += sum(char.isalpha() and char.isascii() for char in line)
            words_count += len(line.split())
            lines_count += 1
        print(f'{letters_count} letters \n{words_count} words\n{lines_count} lines')



statistic('file.txt')