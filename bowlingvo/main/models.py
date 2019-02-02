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
    tag = models.CharField(max_length=32)

    def __str__(self):
        return str(self.id)


class Translation_Unit(models.Model):
    objects = models.Manager()
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    word_ru = models.CharField(max_length=64)
    word_for = models.CharField(max_length=64)

class Theory_Unit(models.Model): #wrong model, fix, add lesson type (G, L) and two different sections for grammar and lexis
    objects = models.Manager()
    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    theory = models.TextField()


class Finished_Lesson(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Blanks(models.Model): # rename to 'Phrase'
    objects = models.Manager()
    tag = models.CharField(max_length=32)
    blank = models.TextField()


class User_Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
    avatar = models.TextField(default='main/images/user.png')
    last_lang = models.IntegerField(default=0)