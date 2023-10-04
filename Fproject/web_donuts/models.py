from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Donut(models.Model):
    CATEGORY_CHOICES = (
        ('Chocolate', 'Chocolate'),
        ('Vanilla', 'Vanilla'),
        ('Fruit-filled','Fruit-filled'),
        ('Red velvet','Red velvet'),
        ('Salted caramel','Salted caramel'),
        ('Peanut butter','Peanut Butter'),
        ('Matcha','Matcha')
    )

    category = models.CharField(max_length = 50,choices = CATEGORY_CHOICES )
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    image = models.ImageField(upload_to = 'donut_images/')
    description = models.TextField(default = 'Ingredients:')

    def __str__(self):
        return self.name
    

# class CartItem(models.Model):
#     product = models.ForeignKey('Donut', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

# class Cart(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     items = models.ManyToManyField(CartItem)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
    
class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    donut = models.ForeignKey(Donut,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.quantity} x {self.donut.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.TextField()