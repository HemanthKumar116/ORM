from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    director = models.CharField(max_length=100)
    rating = models.FloatField()
    duration = models.IntegerField()
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title