from django.contrib import admin

from projects.Course.models import Course, StudCour, TeachCour

admin.site.register(Course)
admin.site.register(StudCour)
admin.site.register(TeachCour)
