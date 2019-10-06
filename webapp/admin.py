from django.contrib import admin
from . models import employees
# Register your models here.

admin.site.register(employees)
#serializer is used to convert the data into json format
