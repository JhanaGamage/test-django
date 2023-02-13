from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    name = models.fields.CharField(max_length=100, primary_key=True)
    genre = models.fields.CharField(max_length=1, default="0")
    biography = models.fields.CharField(max_length=100, default="")
    year_formed = models.fields.IntegerField(max_length=100, default="")
    active = models.fields.BooleanField(default=False)
    official_homepage = models.fields.URLField(max_length=1000, default="")
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default="S")
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)], 
        default=2000
    )
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

    def __str__(self):
        return f'{self.name}' # Define display name on admin site

class Listing(models.Model):
    name = models.fields.CharField(max_length=100, default="hello", primary_key=True)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)