from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from LibraryApp.models import Admin, Book


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('AdminId', 'AdminName', 'AdminPassword',
                  'AdminEmail', 'isAdmin')


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('BookId', 'BookName', 'BookCategory', 'BookAuthor')
