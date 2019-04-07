
import importlib
from ..models import *
import base64
import json


def task_gen(lesson_id):
    if lesson_id == 'frame':
        tasks = [{'type': 'choice', 'text': ['sunday'], 'answer': 'воскресенье', 'choices': ['четверг', 'воскресенье', 'пятница', 'неделя']},
                {'type': 'choice', 'text': ['mondays'], 'answer': 'понедельники', 'choices': ['понедельники', 'вторники', 'четверги', 'среды']},
                {'type': 'choice', 'text': ['вторники'], 'answer': 'tuesdays', 'choices': ['sundays', 'weeks', 'tuesdays', 'mondays']},
                {'type': 'choice', 'text': ['суббота'], 'answer': 'saturday', 'choices': ['saturday', 'friday', 'thursday', 'sunday']},
                {'type': 'choice', 'text': ['weeks'], 'answer': 'недели', 'choices': ['вторники', 'субботы', 'среды', 'недели']},
                {'type': 'choice', 'text': ['пятницы'], 'answer': 'fridays', 'choices': ['saturdays', 'sundays', 'fridays', 'thursdays']},
                {'type': 'choice', 'text': ['четверги'], 'answer': 'thursdays', 'choices': ['fridays', 'sundays', 'thursdays', 'wednesdays']},
                {'type': 'input', 'answer': 'воскресенье', 'text': ['This ', 'sunday', " I'll go to London.", 'В это ', ' я поеду в Лондон.']},
                {'type': 'choice', 'text': ['wednesday'], 'answer': 'среда', 'choices': ['неделя', 'четверг', 'среда', 'понедельник']}]
        ans = [task['answer'] for task in tasks]
        d = dict(attempt=1, answers=ans)
        j = json.dumps(d)
        encoded = base64.b64encode(j.encode()).decode()
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
