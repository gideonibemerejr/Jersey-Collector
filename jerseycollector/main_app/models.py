from django.db import models

# Create your models here.


class Jersey(models.Model):
    year = models.CharField(max_length=5)
    club = models.CharField(max_length=100)
    player = models.CharField(max_length=100)
    kit_type = models.CharField(max_length=100)
    sleeve_length = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=5)

    def __str__(self):
        return self.name


jerseys = [
   Jersey( year='08-09', club='Manchester United', player='Cristiano Ronaldo', kit_type='Home', sleeve_length='L', price=150.00, size='XL'),
    Jersey(year='98-99', club='AS Roma', player='Francesco Totti', kit_type='Away', sleeve_length='S', price=129.99, size='XS'),
    Jersey(year='01-02', club='Arsenal', player='Thierry Henry', kit_type='Home', sleeve_length='L', price=69.99, size='L'),
    Jersey(year='04-05', club='Real Madrid', player='Zinedine Zidane', kit_type='Home', sleeve_length='L', price=129.99, size='XXXL'),
    Jersey(year='11-12', club='Inter Milan', player='Javier Zanetti', kit_type='Third', sleeve_length='L', price=89.99, size='M'),
]
