from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.


class Teammate(models.Model):
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('teammates_detail', kwargs={'pk': self.id})

class Jersey(models.Model):
    player = models.CharField(max_length=100)
    year = models.CharField(max_length=7)
    club = models.CharField(max_length=100)
    kit_type = models.CharField(max_length=5)
    sleeve_length = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=5)
    teammates = models.ManyToManyField(Teammate)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.year} {self.club} {self.player}'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'jersey_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    jersey = models.ForeignKey(Jersey, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for jersey_id: {self.jersey_id} @{self.url}"







