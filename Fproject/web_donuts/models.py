from django.db import models

# Create your models here.
class Donut(models.Model):
    CATEGORY_CHOICES = (
        ('chocolate', 'Chocolate'),
        ('vanilla', 'Vanilla'),
        ('cinnamon sugar','Cinnamon Sugar'),
        ('fruit-filled','Fruit-filled'),
        ('red velvet','Red velvet'),
        ('salted-caramel','Salted caramel'),
        ('peanut-butter','Peanut Butter'),
        ('mocha','Mocha')
    )

    category = models.CharField(max_length = 50,choices = CATEGORY_CHOICES )
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    image = models.ImageField(upload_to = 'donut_images/')

    def __str__(self):
        return self.name