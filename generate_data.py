import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django

django.setup()
from faker import Faker
from course.models import Subject, Speciality


def generate_subjects(f):
    for _ in range(20):
        Subject.objects.create(name=f.name())


def generate_speciality(f):
    for _ in range(20):
        spec = Speciality.objects.create(name=f.name(), code=f.ipv4_private())
        subjects = []
        for i in range(1,random.randint(1, 20)):
            subjects.append(Subject.objects.get(id=i))
        spec.subjects.set(subjects)


if __name__ == '__main__':
    f = Faker()
    # generate_subjects(f)
    generate_speciality(f)