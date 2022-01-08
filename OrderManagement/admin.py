from django.contrib import admin

# Register your models here.

from .models import PersonnelList
admin.site.register(PersonnelList)

from .models import StudentList
admin.site.register(StudentList)
