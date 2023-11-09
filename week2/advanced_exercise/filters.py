import itertools

def filter_by_genre(books, genre):
    for book in books:
        if book["genre"] == genre:
            yield book

def top_rated_books(books, min_rating):
    for book in books:
        if book["rating"] >= min_rating:
            yield book

def sort_books(books, key):
    return sorted(books, key=lambda x: x[key])

def count_authors(books):
    author_counts = {}
    for book in books:
        author = book["author"]
        author_counts[author] = author_counts.get(author, 0) + 1
    return author_counts

def limit_results(limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return itertools.islice(func(*args, **kwargs), limit)
        return wrapper
    return decorator

list_of_books = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "rating": 4.27,
        "year": 1960,
        "genre": "Fiction"
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "rating": 4.16,
        "year": 1949,
        "genre": "Fiction"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "rating": 3.93,
        "year": 1925,
        "genre": "Fiction"
    },
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "rating": 4.30,
        "year": 1945,
        "genre": "	Political satire"
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "rating": 4.26,
        "year": 1813,
        "genre": "Romance"
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "rating": 4.28,
        "year": 1937,
        "genre": "Fantasy"
    }
]

# Filter books by genre
filtered_books = filter_by_genre(list_of_books, "Fiction")
for book in filtered_books:
    print("fiction filtered book :" , book)

# Get top-rated books
top_books = top_rated_books(list_of_books, 4.2)
for book in top_books:
    print(book)

# Sort books by title
sorted_books = sort_books(list_of_books, "title")
for book in sorted_books:
    print(book)

# Count authors
author_counts = count_authors(list_of_books)
for author, count in author_counts.items():
    print(f"{author}: {count} books")

# Apply the limit decorator
@limit_results(3)
def limited_books():
    for book in list_of_books:
        yield book

limited_books = limited_books()
for book in limited_books:
    print(book)
    
    
