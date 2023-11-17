
def read_end(lines, file):
    with open(file, 'r', encoding='utf-8') as f:
        all_lines = f.readlines()

        print(f'Последние {lines} строк из файла {file}: ')
        for line in all_lines[-lines:]:
            print(line.strip())


read_end(5, 'article.txt')

