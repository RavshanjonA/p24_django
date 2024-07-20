from django.urls import path

from student.views import student_books_view

app_name = "student"
urlpatterns = [
    path("student-book/", student_books_view, name="books"),
]
