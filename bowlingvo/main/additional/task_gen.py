from ..models import *
import random


def lex_task_gen(lesson_id):
    my_lesson = Lesson.objects.get(pk=lesson_id)
    my_words = WordRus.objects.all().filter(lesson_id=lesson_id)
    #my_tag = my_lesson.tag
    #available_blanks = Blanks.objects.all().filter(tag=my_tag)
    tasks = []
    for i in range(len(my_words)):
        type = random.randint(0, 1)
        if type == 0:
            words = list()
            for word in my_words:
                if word.word_for == my_words[i].word_for:
                    continue
                words.append(word.word_for)
            choices = random.sample(words, 3)
            pos = random.randint(0, 3)
            choices.insert(pos, my_words[i].word_for)
            tasks.append({'type': 'choice', 'word': my_words[i].word_ru, 'answer': my_words[i].word_for, 'choices': choices})
        else:
            tasks.append({'type': 'input', 'word': my_words[i].word_ru, 'answer': my_words[i].word_for})
    return tasks
