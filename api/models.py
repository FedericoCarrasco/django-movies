from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200, null=True)

class Character(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    weight = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    story = models.TextField(null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=200, null=True)
    release_date = models.DateField(null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=2, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True)
    characters = models.ManyToManyField(Character, null=True)

