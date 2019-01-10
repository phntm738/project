from ..models import Lesson, Translation_Unit, Blanks
import random


def lex_task_gen(lesson_id):
    my_lesson = Lesson.objects.get(pk=lesson_id)
    my_words = Translation_Unit.objects.all().filter(lesson_id=lesson_id)
    my_tag = my_lesson.tag
    available_blanks = Blanks.objects.all().filter(tag=my_tag)
    tasks = []
    for i in range(len(my_words)):
        type = random.randint(0, 1)
        if type == 0:
            words = []
            for j in my_words:
                words.append(my_words[j].word_for)
            choices = random.sample(words, 3)
            pos = random.randint(0, 3)
            choices.insert(pos, my_words[i].word_for)
            tasks.append({'type': 'choice', 'word': my_words[i].word_rus, 'answer': my_words[i].word_for, 'choices': choices})
        else:
            tasks.append({'type': 'input', 'word': my_words[i].word_rus, 'answer': my_words[i].word_for})
    return tasks


def test():
    print(lex_task_gen(1))
