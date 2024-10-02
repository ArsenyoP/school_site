from django.contrib import admin

from main_page.models import about_page, global_data, sections, gallery

admin.site.register(sections)
admin.site.register(about_page)
admin.site.register(global_data)
admin.site.register(gallery)