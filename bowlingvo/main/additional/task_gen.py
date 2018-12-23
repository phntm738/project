from ..models import Section
from ..models import Lesson
from ..models import Translation_Unit
from ..models import Theory_Unit


def lex_task_gen(lesson_id):
    my_lesson = Lesson.objects.get(pk=lesson_id)
    my_words = Translation_Unit.objects.get(lesson_id=lesson_id)