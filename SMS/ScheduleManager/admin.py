from django.contrib import admin
from .models import *

admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)