from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    type = models.IntegerField(choices=(
        (1, 'admin'),
        (2, 'client'),
    ), default=2)
    phone = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
   
    def __str__(self):
        return self.username
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Slider(models.Model):
    image = models.ImageField(upload_to="Slider/")
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=60)

class Category(models.Model):
    name = models.CharField(max_length=100)
   
    def __str__(self):
        return self.name

class Wears(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="Wears")
    image2 = models.ImageField(upload_to="Wears", blank=True, null=True)
    image3 = models.ImageField(upload_to="Wears", blank=True, null=True)
    image4 = models.ImageField(upload_to="Wears", blank=True, null=True)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()

class WearsProduction(models.Model):
    wears = models.ForeignKey(Wears, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    day = models.DateField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Wears, on_delete=models.CASCADE)
    price = models.IntegerField()
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Wears, on_delete=models.CASCADE)

class Cash(models.Model):
    cash = models.IntegerField(default=0)

class Buy(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    day = models.DateField(auto_now_add=True)

class NewsLetter(models.Model):
    email = models.EmailField()

class Info(models.Model):
    logo = models.ImageField(upload_to="Info/")
    text = models.TextField()
    telegram_link = models.CharField(max_length=500)
    instagram_link = models.CharField(max_length=500)
    facebook_link = models.CharField(max_length=500)







