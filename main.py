import os
import csv

# Путь к файлу относительно расположения скрипта
BASE_DIR = os.path.dirname(os.path.abspath("books.csv"))

def parse_row(row):
    return [row[0], row[1], row[2], int(row[3]), float(row[4])]

def get_books(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        return list(map(parse_row, reader))

books = get_books("books.csv")
print("Задание 1:", books)

def filtered_books(books, keyword):
    matches = filter(lambda b: keyword.lower() in b[1].lower(), books)
    return list(map(
        lambda b: [b[0], f"{b[1]}, {b[2]}", b[3], b[4]],
        matches
    ))

result = filtered_books(books, "python")
print("Задание 2:", result)

def books_total(books):
    return list(map(
        lambda b: (b[0], b[3] * b[4]),
        books
    ))

totals = books_total(books)
print("Задание 3:", totals)

input('Enter....')
