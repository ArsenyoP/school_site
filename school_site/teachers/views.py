from lib2to3.fixes.fix_input import context

from django.urls import reverse

from django.shortcuts import render

from teachers.forms import subjects_add, teacher_add
from teachers.models import subjects,teachers

from django.http import HttpResponseRedirect
from django.shortcuts import render


def teachers_catalog(request):
    subjects_all = subjects.objects.all()
    teachers_all = teachers.objects.all()
    context = {
        "subjects": subjects_all,
        "teachers": teachers_all
    }
    return render(request, "teachers/teachers.html", context)

def add_subject(request):
    if request.method == "POST":
        form = subjects_add(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = subjects_add()
        print("Помилка валідації")
    context = {
        "form": form
    }
    return render(request, "teachers/Add_subject.html", context)

def add_teacher(request):
    if request.method == "POST":
        form = teacher_add(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            print("Помилка валідації")
    else:
        form = teacher_add()
    context = {
        "form": form
    }
    return render(request, "teachers/add_teacher.html", context)