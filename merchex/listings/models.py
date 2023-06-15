from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from django.db import models

class Band(models.Model) :
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices,max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900),MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
class Listing(models.Model) :

    class Type(models.TextChoices):
        records = 'Records'
        clothing = 'Clothing'
        posters = 'Posters'
        miscellaneous = 'Miscellaneous'
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=250)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True,blank=True)
    types = models.fields.CharField(choices=Type.choices, max_length=30)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.title}'

