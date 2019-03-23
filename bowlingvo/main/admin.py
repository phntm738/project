from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Language)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(TheoryUnit)
admin.site.register(FinishedLesson)
admin.site.register(FinishedSection)
admin.site.register(Word)
admin.site.register(Phrase)
admin.site.register(Key2Lesson)


