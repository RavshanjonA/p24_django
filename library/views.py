from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    return render(request, "home.html")

def authors_view(request):
    return render(request, "library/authors.html")

def books_view(request):
    return render(request, "library/books.html")

