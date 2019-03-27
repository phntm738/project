from django.contrib import admin

# Register your models here.
from .models import *


'''class WordsInLine(admin.TabularInline):
    model = Word
    extra = 5

class PhrasesInLine(admin.TabularInline):
    model = Phrase
    extra = 1

class Key2LessonInLine(admin.TabularInline):
    model = Key2Lesson
    extra = 5

class LessonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Lesson Info', {'fields':['section', 'order', 'tag']})
        ]
    inlines = [WordsInLine]'''

admin.site.register(Language)
admin.site.register(Section)
admin.site.register(Lesson)
admin.site.register(TheoryUnit)
admin.site.register(FinishedLesson)
admin.site.register(FinishedSection)
admin.site.register(Word)
admin.site.register(Phrase)
admin.site.register(Key2Lesson)


