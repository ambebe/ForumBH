from django.db import models
from django.contrib.auth.models import User

class Sup(models.Model):
    gmail = models.CharField(max_length=100)
    support = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    release_date = models.DateField()
    pages = models.IntegerField()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    icon = models.ImageField(upload_to="myfirstpage/images/")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)