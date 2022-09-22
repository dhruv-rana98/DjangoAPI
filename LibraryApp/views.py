# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from LibraryApp.models import Admin, Book
from LibraryApp.serializers import AdminSerializers, BookSerializers


@csrf_exempt
def bookApi(request, id=0):
    if request.method == 'GET':
        books = Book.objects.all()
        book_serializer = BookSerializers(books, many=True)
        return JsonResponse(book_serializer.data, safe=False)
    elif request.method == 'POST':
        bookdata = JSONParser().parse(request)
        book_serializer = BookSerializers(data=bookdata)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Book added successfully", safe=False)
        return JsonResponse("Failed to add the book", safe=False)
    elif request.method == 'PUT':
        bookdata = JSONParser().parse(request)
        book = Book.objects.get(BookId=bookdata['BookId'])
        book_serializer = BookSerializers(book, data=bookdata)
        if book_serializer.is_valid():
            book_serializer.save()
            return JsonResponse("Book modified successfully", safe=False)
        return JsonResponse("Failed to modify book", safe=False)
    elif request.method == 'DELETE':
        book = Book.objects.get(BookId=id)
        book.delete()
        return JsonResponse('Book Deleted Successfully',  safe=False)


@csrf_exempt
def adminApi(request, id=0):
    if request.method == 'GET':
        admin = Admin.objects.all()
        admin_serializer = AdminSerializers(admin, many=True)
        return JsonResponse(admin_serializer.data, safe=False)
    elif request.method == 'POST':
        admindata = JSONParser().parse(request)
        admin_serializer = AdminSerializers(data=admindata)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("User Added Successfully", safe=False)
        return JsonResponse("Failed to add the user", safe=False)
    elif request.method == 'PUT':
        admindata = JSONParser().parse(request)
        admin = Admin.objects.get(AdminId=admindata['AdminId'])
        admin_serializer = AdminSerializers(admin, data=admindata)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("User modified successfully", safe=False)
        return JsonResponse("Failed to modify user", safe=False)
    elif request.method == 'DELETE':
        admin = Admin.objects.get(AdminId=id)
        admin.delete()
        return JsonResponse('Admin Deleted Successfully',  safe=False)
