from django.db import models

# Create your models here.


class Jersey:
    def __init__(self, year, club, player, kit_type, sleeve_length, price, size):
        self.year = year
        self.club = club
        self.player = player
        self.kit_type = kit_type + ' Shirt'
        self.sleeve_length = sleeve_length + '/S'
        self.price = '$ ' + price
        self.size = size


jerseys = [
    Jersey('08-09', 'Manchester United',
           'Cristiano Ronaldo', 'Home', 'L', '150.00', 'XL'),
    Jersey('98-99', 'AS Roma', 'Francesco Totti', 'Away', 'S', '129.99', 'XS'),
    Jersey('01-02', 'Arsenal', 'Thierry Henry', 'Home', 'L', '69.99', 'L'),
    Jersey('04-05', 'Real Madrid', 'Zinedine Zidane',
           'Home', 'L', '129.99', 'XXXL'),
    Jersey('11-12', 'Inter Milan', 'Javier Zanetti', 'Home', 'L', '89.99', 'M'),
]
