from django.db import models
from django.urls import reverse

# Create your models here.
HASCAUGHT = (
    ('Y', 'Yes'),
    ('N','No'),
    ('E','Escaped')
)


RARITY = (
    ('Common','Common'),
    ('Uncommon','Uncommon'),
    ('Rare','Rare'),
    ('Ultra Rare','Ultra Rare'),
    ('Legendary','Legendary'),
    ('Mythical','Mythical')
)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    element = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('details', kwargs={'pokemon_id': self.id})



class Caught(models.Model):
    caught = models.CharField(
        max_length=1,
        choices= HASCAUGHT,
        default=HASCAUGHT[0][1]
    )
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)



def __str__(self):
    return f"{self.get_hascaught_display()}"






class Rarity(models.Model):
    rarity = models.CharField(
        max_length=10,
        choices= RARITY,
        default=None
)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.get_rarity_display()}"
