# copy and paste the below queries into the django shell to see them in action. Feel free to experiment with making your own queries too!

from django.contrib.auth.models import User
from bookclub.models import Reader, Book, Genre, Reading, Quote

# One-to-One: Reader ↔ User

reader = Reader.objects.get(id=1)
print(f"{reader}: {object.__repr__(reader)}")

username = reader.user.username
print(f"{username}: {object.__repr__(username)}")

user = User.objects.get(id=1)
print(f"{user}: {object.__repr__(user)}")

reader = user.reader
print(f"{reader}: {object.__repr__(reader)}")

books = reader.books.all()
print(f"{books}: {object.__repr__(books)}")

# One-to-Many: Book → Quote
book = Book.objects.get(id=1)
print(f"{book}: {object.__repr__(book)}")

quotes = book.quote_set.all()
print(f"{quotes}: {object.__repr__(quotes)}")

quote = Quote.objects.get(id=1)
print(f"{quote}: {quote.__repr__()}")

book = quote.book
print(f"{book}: {book.__repr__()}")

# Many-to-Many: Book ↔ Genre
book = Book.objects.get(id=1)
print(f"{book}: {object.__repr__(book)}")

genres = book.genres.all()
print(f"{genres}: {object.__repr__(genres)}")

genre = Genre.objects.get(id=1)
print(f"{genre}: {object.__repr__(genre)}")

books = genre.book_set.all()
print(f"{books}: {object.__repr__(books)}")

# Many-to-Many with Through Table: Reader ↔ Book via Reading
reader = Reader.objects.get(id=1)
print(f"{reader}: {object.__repr__(reader)}")

book = Book.objects.get(id=1)
print(f"{book}: {object.__repr__(book)}")

books_for_reader = Book.objects.filter(reading__reader=reader)
print(f"{books_for_reader}: {object.__repr__(books_for_reader)}")

readers_for_book = Reader.objects.filter(reading__book=book)
print(f"{readers_for_book}: {object.__repr__(readers_for_book)}")

reading = Reading.objects.get(reader=reader, book=book)
print(f"{reading}: {object.__repr__(reading)}")

start_date_of_reading = reading.date_started
print(f"{start_date_of_reading}: {object.__repr__(start_date_of_reading)}")

all_readings_for_reader = reader.reading_set.all()
print(f"{all_readings_for_reader}: {object.__repr__(all_readings_for_reader)}")

all_readings_for_reader_filter = Reading.objects.filter(reader=reader)
print(
    f"{all_readings_for_reader_filter}: {object.__repr__(all_readings_for_reader_filter)}"
)
