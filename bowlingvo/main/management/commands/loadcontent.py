from django.core.management.base import BaseCommand, CommandError
from ...models import Word, Phrase, Key2Lesson
import os
from ...additional import content


class Command(BaseCommand):
    help = "loads site content from 'additional/content' directory into database"

    def list_languages(self):
        return getattr(content, '__all__')

    def add_arguments(self, parser):
        parser.add_argument('language', nargs='*', type=str)

        parser.add_argument(
            '-a', '--all',
            action='store_true',
            dest='all',
            help='loads all languages'
        )

    def handle(self, *args, **options):
        Word.objects.all().delete()
        Phrase.objects.all().delete()
        Key2Lesson.objects.all().delete()
        self.stdout.write('Database cleared...')

        if not options['language'] and not options['all']:
            self.stdout.write('Available languages:')
            self.stdout.write('\n'.join(['\t' + s for s in self.list_languages()]))
            return
        elif options['all']:
            options['language'] = self.list_languages()

        languages = options['language']
        for lang in languages:
            self.stdout.write('Loading language content for %s...' % lang)
            lang_main = getattr(getattr(content, lang), 'main')
            lang_main()
            self.stdout.write('OK...')
        self.stdout.write('Done')
