from django.contrib import admin

# Register your models here.
from . models import Student

admin.site.site_header = 'Zago Admin Area'
admin.site.index_title = 'YOUR ZONE'

admin.site.register(Student)
