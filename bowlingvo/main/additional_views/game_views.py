from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
import json
import base64
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models import *
from django.views import View
from ..additional.task_gen import task_gen
from django.urls import reverse


class GameStartView(LoginRequiredMixin, View):
    login_url = '/main/login'
    template_name = 'main/startgame.html'

    def get(self, request, language_name):
        return render(request, self.template_name, {'language': language_name})

    def post(self, request, language_name):
        frames = int(request.POST.get('frames'))
        max_frames = len([fs for fs in FinishedSection.objects.filter(user=request.user) if fs.section.language.url_name == language_name])
        if 1 <= frames <= min(max_frames, 10):
            FrameRecord.objects.filter(user=request.user).delete()
            game = FrameRecord(user=request.user, max_frames=frames)
            game.save()
            return redirect(reverse('game', kwargs={'language_name': language_name}))
        elif frames < 1:
            error_message = 'Число фреймов должно быть не меньше 1'
        else:
            error_message = 'Число фреймов должно быть не больше 10 и не больше числа пройденных секций (%d)' % max_frames
        return render(request, self.template_name, {'language': language_name, 'error_message': error_message})


class GameView(LoginRequiredMixin, View):
    login_url = '/main/login'
    template_name = 'main/frame.html'

    def get(self, request, language_name):
        cur_game = FrameRecord.objects.get(user=request.user)
        cur_game.cur_frame += 1
        if cur_game.frame_score != 0:
            cur_game.frame_score = 0
        cur_frame = cur_game.cur_frame
        max_frames = cur_game.max_frames
        if cur_frame > max_frames:
            return redirect(reverse('endgame', kwargs={'language_name': language_name}))
        encoded, tasks = task_gen('frame', request.user, language_name)
        cur_game.save()
        return render(request, self.template_name, {'tasks': tasks, 'encoded': encoded, 'language': language_name, 'cur_frame': cur_frame, 'max_frames': max_frames})

    def score_append(self, request, score):
        cur_game = FrameRecord.objects.get(user=request.user)
        score_table = json.loads(cur_game.score_table)
        if score == 'strike':
            score_table.append(['x'])
        elif score == 'spare':
            score_table[-1].append('/')
        else:
            if len(score_table) == 0 or len(score_table[-1]) == 2 or score_table[-1] == ['x']:
                score_table.append([score])
            else:
                score_table[-1].append(score)
        cur_game.score_table = json.dumps(score_table)
        cur_game.save()
        return cur_game

    def post(self, request, language_name):
        cur_game = FrameRecord.objects.get(user=request.user)
        encoded = request.POST.get('encoded')
        answers = json.loads(request.POST.get('answers'))
        params = json.loads(base64.b64decode(encoded.encode()).decode())
        ans = []
        score = 0
        for i in range(len(answers)):
            if answers[i][1] == params['answers'][i]:
                ans.append(True)
                if answers[i][0] == 'L':
                    score += 1
                else:
                    score += 2
            else:
                ans.append(False)
        response = {}
        if params['attempt'] == 2:
            if score == 10:
                self.score_append(request, 'spare')
            else:
                self.score_append(request, score-cur_game.frame_score)
            response['end'] = True
            response['score'] = score if score != 10 else 'spare'
        else:
            if score == 10:
                self.score_append(request, 'strike')
                response['end'] = True
                response['score'] = 'strike'
            else:
                cur_game = self.score_append(request, score)
                cur_game.frame_score = score
                cur_game.save()
                response['end'] = False
                params['attempt'] = 2
        response['encoded'] = base64.b64encode(json.dumps(params).encode()).decode()
        response['ans'] = ans
        response = json.dumps(response)
        return HttpResponse(response)


def count_score(score_table):
    st = []
    for frame in score_table:
        for throw in frame:
            st.append(throw)
    score = 0
    for i in range(len(st)):
        throw = st[i]
        if throw == 'x':
            score += 10
            for j in range(i+1, len(st)):
                if j - i == 3:
                    break
                next_throw = st[j]
                if next_throw == 'x':
                    next_throw = 10
                elif next_throw == '/':
                    next_throw = 10 - st[j-1]
                score += next_throw
        elif throw == '/':
            score += 10 - st[i-1]
            if i != len(st) - 1:
                next_throw = st[i+1]
                if next_throw == 'x':
                    next_throw = 10
                score += next_throw
        else:
            score += throw
    return score





@login_required(login_url='/main/login')
def endgame(request, language_name):
    game = FrameRecord.objects.get(user=request.user)
    score_table = json.loads(game.score_table)
    score = count_score(score_table)
    game.delete()
    profile = UserProfile.objects.get(user=request.user)
    profile.score += score
    profile.save()
    language_title = Language.objects.get(url_name=language_name).name
    return render(request, 'main/endgame.html', {'language_title': language_title, 'score': score, 'language_name': language_name})