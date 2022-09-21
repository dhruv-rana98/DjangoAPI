from pyexpat import model
from django.db import models

# Create your models here.


class Admin(models.Model):
    AdminId = models.AutoField(primary_key=True)
    AdminName = models.CharField(max_length=500)
    AdminPassword = models.CharField(max_length=30)
    AdminEmail = models.EmailField(max_length=45)
    isAdmin = models.BooleanField(False)


class Book(models.Model):
    BookId = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=500)
    BookCategory = models.CharField(max_length=500)
    BookAuthor = models.CharField(max_length=500)
