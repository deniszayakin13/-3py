def filtered_books(books, keyword):
    matches = filter(lambda b: keyword.lower() in b[1].lower(), books)
    return list(map(
        lambda b: [b[0], f"{b[1]}, {b[2]}", b[3], b[4]],
        matches
    ))

books = get_books("books.csv")
result = filtered_books(books, "python")
print(result)
