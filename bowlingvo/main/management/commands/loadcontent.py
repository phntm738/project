from django.core.management.base import BaseCommand
from ...models import Word, Phrase, Key2Lesson
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
