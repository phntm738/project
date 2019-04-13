from ...models import *
import random
from types import SimpleNamespace as SN
import base64
import json


class BaseGenerator:
    language = ''

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
        theory = TheoryUnit.objects.get(lesson=lesson).theory
        inp_tasks = list(TheoryTask.objects.filter(lesson=lesson, type='I'))
        ch_tasks = list(TheoryTask.objects.filter(lesson=lesson, type='C'))
        all_choices = [task.answer for task in ch_tasks]
        tasks = []
        while len(tasks) < 10 and (inp_tasks or ch_tasks):
            type_per = random.randint(0, 1)
            if type_per and ch_tasks:
                ch_task = random.choice(ch_tasks)
                ch_tasks.remove(ch_task)
                task = {'type': 'choice', 'text': [ch_task.task], 'answer': ch_task.answer}
                self_choices = list(all_choices)
                self_choices.remove(ch_task.answer)
                choices = random.sample(self_choices, 3)
                pos = random.randint(0, 3)
                choices.insert(pos, ch_task.answer)
                task['choices'] = choices
                tasks.append(task)
            elif not type_per and inp_tasks:
                inp_task = random.choice(inp_tasks)
                inp_tasks.remove(inp_task)
                text = list(inp_task.task.split('{}'))
                task = {'type': 'input', 'text': text, 'answer': inp_task.answer}
                tasks.append(task)
        return theory, tasks

    def gen_lex(self, lesson):
        type_per = random.randint(0, 1)
        if type_per:
            keys = random.sample(list(lesson.key2lesson_set.filter(key__startswith='w')), 4)
            words = [[Word.objects.get(key=key.key, language='russian'), Word.objects.get(key=key.key, language=self.language)] for key in keys]
            task_pos = random.randint(0, 3)
            task_words = words.pop(task_pos)
            base_lang_rus = random.randint(0, 1)
            use_plur = random.randint(0, 1)
            if base_lang_rus:
                base = task_words[0]
                trans = task_words[1]
                choice_words = [w[1] for w in words]
            else:
                base = task_words[1]
                trans = task_words[0]
                choice_words = [w[0] for w in words]
            if use_plur:
                text = base.plur_form
                ans = trans.plur_form
                choices = [w.plur_form for w in choice_words]
            else:
                text = base.sing_form
                ans = trans.sing_form
                choices = [w.sing_form for w in choice_words]
            pos = random.randint(0, 3)
            choices.insert(pos, ans)
            task = dict(type='choice', text=[text], choices=choices)
        else:
            key = random.choice(list(lesson.key2lesson_set.filter(key__startswith='p')))
            base_lang_rus = random.randint(0, 1)
            if base_lang_rus:
                base = Phrase.objects.get(key=key.key, language='russian')
                trans = Phrase.objects.get(key=key.key, language=self.language)
            else:
                base = Phrase.objects.get(key=key.key, language=self.language)
                trans = Phrase.objects.get(key=key.key, language='russian')
            parts = base.text.split('{}')
            text = [parts[0]] + [base.answer] + [parts[1]]
            parts = trans.text.split('{}')
            text.append(parts[0])
            text.append(parts[1])
            task = dict(type='input', text=text)
            ans = trans.answer
        task['tasktype'] = 'L'
        return task, ans

    def gen_gram(self, lesson):
        type_per = random.randint(0, 1)
        if type_per:
            ch_tasks = random.sample(list(TheoryTask.objects.filter(lesson=lesson, type='C')), 4)
            tasks_pos = random.randint(0, 3)
            ch_task = ch_tasks.pop(tasks_pos)
            choices = [task.answer for task in ch_task]
            pos = random.randint(0, 3)
            choices.insert(pos, ch_task.answer)
            task = dict(type='choice', text=[ch_task.task], choices=choices)
            ans = ch_task.answer
        else:
            inp_task = random.choice(list(TheoryTask.objects.filter(lesson=lesson, type='I')))
            text = list(inp_task.task.split('{}'))
            task = dict(type='input', text=text)
            ans = inp_task.answer
        task['tasktype'] = 'G'
        return task, ans

    def frame(self, user):
        sections = [s.section for s in FinishedSection.objects.filter(user=user)
                   if s.section.language.url_name == self.language]
        pins = 0
        tasks = []
        answers = []
        while pins < 10:
            if pins == 9:
                lex_secs = [s for s in sections if s.sec_type == 'L']
                sec = random.choice(lex_secs)
                pins += 1
            else:
                sec = random.choice(sections)
            les = random.choice(list(sec.lesson_set.all()))
            if sec.sec_type == 'L':
                pins += 1
                task, ans = self.gen_lex(les)
            else:
                pins += 2
                task, ans = self.gen_gram(les)
            tasks.append(task)
            answers.append(ans)
        d = dict(attempt=1, answers=answers)
        j = json.dumps(d)
        encoded = base64.b64encode(j.encode()).decode()
        return encoded, tasks
