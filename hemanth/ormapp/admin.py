from django.contrib import admin

from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'director', 'rating', 'duration', 'language')

admin.site.register(Movie, MovieAdmin)