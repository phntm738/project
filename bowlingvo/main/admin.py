from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Theory_Unit)

