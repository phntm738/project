from ..models import *
from .generators.base import *


def task_gen(lesson_id):
    generator = BaseGenerator()
    lesson = Lesson.objects.get(pk=lesson_id)
    sec = lesson.section
    if sec.sec_type == 'L':
        tasks = generator.lex_tasks(lesson)
    return tasks
