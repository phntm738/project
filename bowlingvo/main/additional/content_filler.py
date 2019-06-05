from .. import models
import random
import string

LANG = ''


class LexContent:
    class Lesson:
        def __init__(self, section, order):
            self.section = section
            try:
                l = models.Lesson.objects.get(section=section.section, order=order)
            except models.Lesson.DoesNotExist:
                l = models.Lesson(section=section.section, order=order)
                l.save()
            self.lesson = l

        def word(self, sing, plur, fsing, fplur):
            try:
                w = models.Word.objects.get(sing_form=sing, plur_form=plur)
                key = w.key
            except models.Word.DoesNotExist:
                key = 'w' + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(9)])
                w = models.Word(key=key, language='russian', sing_form=sing, plur_form=plur)
                w.save()
            try:
                wf = models.Word.objects.get(sing_form=fsing, plur_form=fplur)
                if wf.key != key:
                    wf.key = key
                    wf.save()
            except models.Word.DoesNotExist:
                wf = models.Word(key=key, language=LANG, sing_form=fsing, plur_form=fplur)
                wf.save()
            try:
                k = models.Key2Lesson.objects.get(lesson=self.lesson, key=key)
            except models.Key2Lesson.DoesNotExist:
                k = models.Key2Lesson(lesson=self.lesson, key=key)
                k.save()
            return self

        def phrase(self, rus, rans, frgn, fans):
            try:
                p = models.Phrase.objects.get(text=rus, answer=rans)
                key = p.key
                if p.text != rus: p.text = rus
                if p.answer != rans: p.answer = rans
            except models.Phrase.DoesNotExist:
                key = 'p' + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(9)])
                p = models.Phrase(key=key, language='russian', text=rus, answer=rans)
            p.save()
            try:
                pf = models.Phrase.objects.get(text=frgn, answer=fans)
                if pf.key != key: pf.key = key
                if p.text != frgn: p.text = frgn
                if p.answer != fans: p.answer = fans
            except models.Phrase.DoesNotExist:
                pf = models.Phrase(key=key, language=LANG, text=frgn, answer=fans)
            pf.save()
            try:
                k = models.Key2Lesson.objects.get(lesson=self.lesson, key=key)
            except models.Key2Lesson.DoesNotExist:
                k = models.Key2Lesson(lesson=self.lesson, key=key)
            k.save()
            return self

        def end(self):
            return self.section

    class Section:
        def __init__(self, language, name, url_name):
            self.language = language
            try:
                s = models.Section.objects.get(language=language.language, name=name, url_name=url_name)
            except models.Section.DoesNotExist:
                s = models.Section(language=language.language, name=name, url_name=url_name)
                s.save()
            self.section = s

        def lesson(self, order):
            return LexContent.Lesson(self, order)

        def end(self):
            return self.language

    def __init__(self, name, url_name):
        try:
            l = models.Language.objects.get(name=name, url_name=url_name)
        except models.Language.DoesNotExist:
            l = models.Language(name=name, url_name=url_name)
            l.save()
        self.language = l

    def section(self, name, url_name):
        return LexContent.Section(self, name, url_name)


class GramContent:
    class Lesson:
        def __init__(self, section, order):
            self.section = section
            try:
                l = models.Lesson.objects.get(section=section.section, order=order)
            except models.Lesson.DoesNotExist:
                l = models.Lesson(section=section.section, order=order)
                l.save()
            self.lesson = l

        def theory(self, theory):
            t = models.TheoryUnit(lesson=self.lesson, theory=theory)
            t.save()
            return self

        def task(self, type, task, answer):
            t = models.TheoryTask(lesson=self.lesson, type=type, task=task, answer=answer)
            t.save()
            return self

        def end(self):
            return self.section

    class Section:
        def __init__(self, language, name, url_name):
            self.language = language
            try:
                s = models.Section.objects.get(language=language.language, name=name, url_name=url_name)
            except models.Section.DoesNotExist:
                s = models.Section(language=language.language, name=name, url_name=url_name, sec_type='G')
                s.save()
            self.section = s

        def lesson(self, order):
            return LexContent.Lesson(self, order)

        def end(self):
            return self.language

    def __init__(self, name, url_name):
        try:
            l = models.Language.objects.get(name=name, url_name=url_name)
        except models.Language.DoesNotExist:
            l = models.Language(name=name, url_name=url_name)
            l.save()
        self.language = l

    def section(self, name, url_name):
        return LexContent.Section(self, name, url_name)
