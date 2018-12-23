from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    objects = models.Manager()
    url_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    objects = models.Manager()
    url_name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    name = models.TextField()
    description = models.TextField()
    sec_type = models.CharField(max_length=1)
    background_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    objects = models.Manager()
    id = models.IntegerField(primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    order = models.IntegerField()
    header = models.TextField()
    footer = models.TextField()

    def __str__(self):
        return self.id


class Tag(models.Model):
    object = models.Manager()
    tag = models.CharField(max_length=32, primary_key=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.tag


class Translation_Unit(models.Model):
    objects = models.Manager()
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    word_ru = models.CharField(max_length=64)
    word_for = models.CharField(max_length=64)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)


class Theory_Unit(models.Model): #wrong model, fix, add lesson type (G, L) and two different sections for grammar and lexis
    objects = models.Manager()
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    theory = models.TextField()


class Finished_Lesson(models.Model):
    objects = models.Manager()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)