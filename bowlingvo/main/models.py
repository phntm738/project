from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

class Section(models.Model):
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    sec_type = models.CharField(max_length=1)
    background_url = models.CharField(max_length=250)

class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    header = models.TextField()
    footer = models.TextField()

class Tag(models.Model):
    tag = models.CharField(max_length=32, primary_key=True, unique=True)
    description = models.TextField()

class Translation_Unit(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    word_ru = models.CharField(max_length=64)
    word_for = models.CharField(max_length=64)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, to_field='tag')

class Theory_Unit(models.Model): #wrong model, fix, add lesson type (G, L) and two different sections for grammar and lexis
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    theory = models.TextField()

class Finished_Lesson(models.Model):
    user_id = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)