from django.contrib import admin

from Course.models import Course, StudCour, TeachCour

admin.site.register(Course)
admin.site.register(StudCour)
admin.site.register(TeachCour)
