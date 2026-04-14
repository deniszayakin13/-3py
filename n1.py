def parse_line(line):
        parts = line.split('|')
        return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]


def get_books(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.strip().split('\n')

    return list(map(parse_line, lines[1:]))

get_books("books.csv")
input("Нажмите Enter, чтобы выйти...")
