# copy and paste the below into the django shell and hit enter
from django.contrib.auth.models import User
from bookclub.models import Reader, Book, Genre, Reading, Quote
from datetime import date

# --- 1. One-to-One: Reader ↔ User
user = User.objects.create_user(username="janedoe")
reader = Reader.objects.create(user=user)

# --- 2. Many-to-Many: Book ↔ Genre
fiction = Genre.objects.create(name="Fiction")
romance = Genre.objects.create(name="Romance")

book1 = Book.objects.create(title="Book One", author="Jackie Doe")
book1.genres.add(fiction, romance)

# --- 3. M2M with Through: Reader ↔ Book via Reading
reading = Reading.objects.create(
    reader=reader, book=book1, date_started=date(2024, 1, 1)
)

# --- 4. One-to-Many: Book → Quote
Quote.objects.create(book=book1, quote="This is the first quote.")
