from ...models import *
import random


class BaseGenerator:

    def lex_tasks(self, lesson):
        sec = lesson.section
        lang = lesson.section.language
        all_words = lesson.wordrus_set.all()
        my_words = []
        for word in all_words:
            my_words.append((word.text, word.wordfor_set.get(language=lang).text))
        tasks = []
        for word in my_words:
            type_per = random.randint(1, 100)
            task = {
                'word': word[0],
                'answer': word[1]
            }
            if type_per > 80:
                task['type'] = 'input'
            else:
                choices = []
                words = list(my_words)
                words.remove(word)
                choice_words = random.sample(words, 3)
                for w in choice_words:
                    choices.append(w[1])
                pos = random.randint(0, 3)
                choices.insert(pos, word[1])
                task['type'] = 'choice'
                task['choices'] = choices
            tasks.append(task)
        return tasks