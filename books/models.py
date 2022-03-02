from django.db import models


# Create your models here.
class Author(models.Model):
    abbrev = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    publicationDate = models.DateField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.RESTRICT)

    def print_authors(self):
        name = ""
        for a in self.authors.all():
            name += a.abbrev + ', '
        name = name[0:-2]   #bo dau , o cuoi
        return name

    def print_publisher(self):
        return self.publisher.name + ", " + self.publisher.country





