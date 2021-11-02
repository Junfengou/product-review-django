from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_photos')
    bio = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    photo = models.ImageField(default='default.jpg', upload_to='product_photos')
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save();

    def __str__(self):
        return str(self.name)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             # related_name='images_created',
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    body = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save();

    def __str__(self):
        return str(self.body)