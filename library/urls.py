from django.urls import path
from .views import home_view, books_view, authors_view

app_name="library"
urlpatterns = [
    path('', home_view, name="home-page"),
    path('books/', books_view, name="books"),
    path('authors/', authors_view, name="authors"),
]
