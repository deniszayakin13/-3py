import os

# Для Colab — файл лежит в текущей рабочей директории
def get_books(file_name):
    # Строим путь относительно текущей папки
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    lines = content.strip().split('\n')
    return list(map(parse_line, lines[1:]))

def parse_line(line):
    parts = line.split('|')
    return [parts[0], parts[1], parts[2], int(parts[3]), float(parts[4])]

# Задание 1
books = get_books("books.csv")
print("Задание 1:", books[:2])

# Задание 2
def filtered_books(books, keyword):
    matches = filter(lambda b: keyword.lower() in b[1].lower(), books)
    return list(map(
        lambda b: [b[0], f"{b[1]}, {b[2]}", b[3], b[4]],
        matches
    ))

result = filtered_books(books, "python")
print("Задание 2:", result)

# Задание 3
def books_total(books):
    return list(map(
        lambda b: (b[0], b[3] * b[4]),
        books
    ))

totals = books_total(books)
print("Задание 3:", totals[:3])
