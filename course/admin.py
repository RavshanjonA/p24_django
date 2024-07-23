from django.contrib import admin

from course.models import Teacher, Speciality, Subject, Student, StudentInfo

admin.site.register([Subject, Speciality, Teacher, Student, StudentInfo])
