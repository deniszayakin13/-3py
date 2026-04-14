def books_total(books):
    return tuple(list(map(
        lambda b: (b[0], b[3] * b[4]),
        books
    )))
books = get_books("books.csv")  
totals = books_total(books)
print(totals)
