from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(Theory_Unit)
admin.site.register(Translation_Unit)
admin.site.register(Tag)
