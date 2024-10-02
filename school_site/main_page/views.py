from django.shortcuts import render
from main_page.models import about_page, global_data, sections, gallery

def index(request):
    data = global_data.objects.all()


    context={
        "main_data" : about_page.objects.all(),
        "sections": sections.objects.all(),
        "gallery": gallery.objects.all(),
        "first_element": data[0],
        "second_element": data[1],
        "third_element": data[2],
        "fours_element": data[3]
    }
    return render(request, "main_page/index.html", context)

