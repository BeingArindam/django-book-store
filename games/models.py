from django.db import models
from django.core.urlresolvers import reverse

class Game(models.Model):
    title = models.CharField(max_length=150)
    production = models.CharField(max_length=150)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)
    release_year = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('games:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.genre
