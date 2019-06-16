from django.db import models
from django.urls import reverse

# Create your models here.


class Teammate(models.Model):
       last_name = models.CharField(max_length=100)

       def __str__(self):
              return self.name
              
class Jersey(models.Model):
    player = models.CharField(max_length=100)
    year = models.CharField(max_length=7)
    club = models.CharField(max_length=100)
    kit_type = models.CharField(max_length=5)
    sleeve_length = models.CharField(max_length=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=5)
    teammate = models.ManyToManyField(Teammate)

    def __str__(self):
        return self.year

    def get_absolute_url(self):
        return reverse('detail', kwargs={'jersey_id': self.id})




