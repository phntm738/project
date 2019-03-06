from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=64)
    url_name = models.CharField(max_length=50)

    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Section(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=64)
    url_name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    sec_type = models.CharField(max_length=1, default='L')

    description = models.TextField(null=True, blank=True)
    background_url = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    objects = models.Manager()

    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    order = models.IntegerField(default=1)
    tag = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.section.name + str(self.order)


class WordRus(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=50) #rename fields
    type = models.CharField(max_length=20, default='noun')
    lessons = models.ManyToManyField(Lesson)
    text = models.TextField()


class WordFor(models.Model):
    objects = models.Manager()

    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    word_rus = models.ForeignKey(WordRus, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.language.name[:4] + '_' + self.word_rus.name


class TheoryUnit(models.Model):
    objects = models.Manager()

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    theory = models.TextField()


class FinishedLesson(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class FinishedSection(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)


class FinishedLanguage(models.Model):
    objects = models.Manager()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)



class Phrase(models.Model):
    objects = models.Manager()

    tag = models.CharField(max_length=32)
    phrase = models.TextField()


class UserProfile(models.Model):
    objects = models.Manager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    score = models.IntegerField(default=0)
    last_lang = models.IntegerField(default=0)
