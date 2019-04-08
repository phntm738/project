from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=64)
    url_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=64)
    url_name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    sec_type = models.CharField(max_length=1, default='L')

    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.language) + '-/-' + str(self.name) + '(' + str(self.sec_type) + ')'


class Lesson(models.Model):
    objects = models.Manager()

    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    order = models.IntegerField(default=1)

    def __str__(self):
        return str(self.section) + '-/-' + str(self.order)


class Key2Lesson(models.Model):
    objects = models.Manager()

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, db_index=True)

    def __str__(self):
        return str(self.lesson) + ' | ' + str(self.key)


class Word(models.Model):
    objects = models.Manager()

    key = models.CharField(max_length=64, db_index=True)
    language = models.CharField(max_length=50)
    sing_form = models.TextField()
    plur_form = models.TextField()

    def __str__(self):
        return str(self.language) + '-/-' + str(self.sing_form)
        

class Phrase(models.Model):
    objects = models.Manager()

    key = models.CharField(max_length=64, db_index=True)
    language = models.CharField(max_length=50)
    text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.key


class TheoryUnit(models.Model):
    objects = models.Manager()

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    theory = models.TextField()


class TheoryTask(models.Model):
    objects = models.Manager()

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, default='C')
    task = models.TextField()
    answer = models.CharField(max_length=32)


class FinishedLesson(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)


class FinishedSection(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)


class FinishedLanguage(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class UserProfile(models.Model):
    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
    last_lang = models.IntegerField(default=0)
