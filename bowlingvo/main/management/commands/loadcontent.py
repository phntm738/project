from django.core.management.base import BaseCommand
from ...models import *
from ...additional import content


class Command(BaseCommand):
    help = "loads site content from 'additional/content' directory into database"

    def list_languages(self):
        return getattr(content, '__all__')

    def handle(self, *args, **options):
        Word.objects.all().delete()
        Phrase.objects.all().delete()
        Key2Lesson.objects.all().delete()
        self.stdout.write('Database cleared...')

        languages = self.list_languages()
        for lang in languages:
            self.stdout.write('Loading language content for %s...' % lang)
            lang_main = getattr(getattr(content, lang), 'main')
            lang_main()
            self.stdout.write('OK...')
        self.stdout.write('Done')

        for les in Lesson.objects.all():
            if (len(les.key2lesson_set.all()) == 0 and les.section.sec_type == 'L') or (len(les.theoryunit_set.all()) == 0 and len(les.theorytask_set.all()) == 0 and les.section.sec_type == 'G'):
                FinishedLesson.objects.filter(lesson=les).delete()
                les.delete()

        for sec in Section.objects.all():
            if len(sec.lesson_set.all()) == 0:
                FinishedSection.objects.filter(section=sec).delete()
                sec.delete()

        for lang in Language.objects.all():
            if len(lang.section_set.all()) == 0:
                FinishedLanguage.objects.filter(language=lang).delete()
                lang.delete()
