from django.contrib import admin


from teachers.models import subjects, teachers


admin.site.register(teachers)
admin.site.register(subjects)
