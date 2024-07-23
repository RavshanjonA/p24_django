from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=56)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subjects = models.ManyToManyField(Subject)

    class Meta:
        verbose_name_plural = "Specialities"
        verbose_name = "Speciality"
        db_table = "speciality"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(max_digits=26, decimal_places=2)  # 211313.42423
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))
    subjects = models.ManyToManyField(Subject, related_name="teachers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentInfo(models.Model):
    student = models.OneToOneField(Student, models.CASCADE, related_name="info")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=28)
    address = models.TextField()

    def __str__(self):
        return f"{self.email}"
