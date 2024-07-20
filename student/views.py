from django.shortcuts import render

def student_books_view(request):
    return render(request,"student/student-book.html")