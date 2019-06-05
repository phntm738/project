import importlib
from ..models import *
import base64
import json


def task_gen(lesson_id, user=None, language=None):
    if lesson_id == 'frame':
        mod_name = 'main.additional.generators.' + language
        module = importlib.import_module(mod_name)
        class_name = language[0].upper() + language[1:]
        generator = getattr(module, class_name + 'Generator')()
        encoded, tasks = generator.frame(user)
        return encoded, tasks
    lesson = Lesson.objects.get(pk=lesson_id)
    sec = lesson.section
    name = sec.language.url_name
    mod_name = 'main.additional.generators.' + name
    module = importlib.import_module(mod_name)
    class_name = name[0].upper() + name[1:]
    generator = getattr(module, class_name + 'Generator')()
    if sec.sec_type == 'L':
        theory, tasks = generator.lex_tasks(lesson)
    else:
        theory, tasks = generator.gram_tasks(lesson)
    return theory, tasks
