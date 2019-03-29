from ...models import *
import random
from types import SimpleNamespace as SN


class BaseGenerator:

    def lex_tasks(self, lesson):
        lang = lesson.section.language
        word_keys = list(lesson.key2lesson_set.filter(key__startswith='w'))
        phrase_keys = list(lesson.key2lesson_set.filter(key__startswith='p'))
        theory = []
        rus_choices_sing = []
        rus_choices_plur = []
        for_choices_sing = []
        for_choices_plur = []
        for word_key in word_keys:
            words = Word.objects.filter(key=word_key.key)
            rwrd = words.get(language='russian')
            fwrd = words.get(language=lang.url_name)
            rus_choices_sing.append(rwrd.sing_form)
            rus_choices_plur.append(rwrd.plur_form)
            for_choices_sing.append(fwrd.sing_form)
            for_choices_plur.append(fwrd.plur_form)
            theory.append(SN(for_sing=fwrd.sing_form, for_plur=fwrd.plur_form,
                             rus_sing=rwrd.sing_form, rus_plur=rwrd.plur_form))

        tasks = []
        for word_key in word_keys:
            task = {'type': 'choice'}
            words = Word.objects.filter(key=word_key.key)
            rwrd = words.get(language='russian')
            fwrd = words.get(language=lang.url_name)
            base_lang_russian = random.choice([0, 1])
            use_plur = random.choice([0, 1])
            if base_lang_russian:
                base_word = rwrd
                trans_word = fwrd
                choice_list = list(for_choices_plur) if use_plur else list(for_choices_sing)
            else:
                base_word = fwrd
                trans_word = rwrd
                choice_list = list(rus_choices_plur) if use_plur else list(rus_choices_sing)
            task['text'] = [base_word.plur_form if use_plur else base_word.sing_form]
            answer = trans_word.plur_form if use_plur else trans_word.sing_form
            task['answer'] = answer
            choice_list.remove(answer)
            choices = random.sample(choice_list, 3)
            pos = random.randint(0, 3)
            choices.insert(pos, answer)
            task['choices'] = choices
            tasks.append(task)

        while len(tasks) < 10 and phrase_keys:
            phrase_key = random.choice(phrase_keys)
            phrase_keys.remove(phrase_key)
            task = {'type': 'input'}
            phrases = Phrase.objects.filter(key=phrase_key.key)
            rphrase = phrases.get(language='russian')
            fphrase = phrases.get(language=lang.url_name)
            base_lang_russian = random.choice([0, 1])
            base_phrase = rphrase if base_lang_russian else fphrase
            trans_phrase = fphrase if base_lang_russian else rphrase
            task['answer'] = trans_phrase.answer
            parts = base_phrase.text.split('{}')
            text = [parts[0]] + [base_phrase.answer] + [parts[1]]
            parts = trans_phrase.text.split('{}')
            text.append(parts[0])
            text.append(parts[1])
            task['text'] = text
            tasks.append(task)
        random.shuffle(tasks)
        return theory, tasks

    def gram_tasks(self, lesson):
        return [], []
