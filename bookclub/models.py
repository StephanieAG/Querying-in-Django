from django.db import models

from django.db import models
from django.contrib.auth.models import User


# Reader model
# One-to-One → User
# Many-to-Many (with through) → Book (via Reading)
class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField("Book", through="Reading")

    def __str__(self):
        return self.user.username


# ----------------------
# Genre model
# Many-to-Many (defined on Book model)
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ----------------------
# Book model
# Type: Many-to-Many → Genre
# Type: Many-to-Many (with through) → defined on Reader model, Reading is the through table
# Type: One-to-Many → Quote
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


# ----------------------
# Reading model
# Through table for the Many-to-Many (between Reader and Book)
# ForeignKey represents a One-to-Many
class Reading(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_started = models.DateField()
    date_finished = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.reader.user.username} - {self.book.title}"


# ----------------------
# Quote model
# One-to-Many → Book
class Quote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quote = models.TextField()

    def __str__(self):
        return f"{self.quote[0:30]}..."
