from django.shortcuts import render

from course.models import Subject, Speciality


def subject_list(request):
    subjects = Subject.objects.all()
    context = {
        "subjects": subjects
    }

    return render(request, "course/subjects.html", context=context)

def speciality_list(request):
    speciality = Speciality.objects.all()
    context = {
        "specialities": speciality
    }

    return render(request, "course/speciality.html", context=context)
def speciality_detail(request, id):
    speciality = Speciality.objects.get(id=id)
    context = {
        "speciality": speciality
    }

    return render(request, "course/speciality_detial.html", context=context)
