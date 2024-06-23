import json
from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.core.signing import Signer
from django.contrib import messages

from common.models.word_model import Word

# Create your views here.

class MatchingView(TemplateView):
    template_name = "matching/index.html"
    signer = Signer()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        word = self.get_randoms_word()
        context.update({
            'word': word,
        })
        return context

    def get_randoms_word(self, word=None):
        next_word = None
        if word:
            next_word = self.get_word_with_start_letter(word[-1])
        else:
            next_word = Word.objects.order_by('?').first().word

        self.request.session['sign'] = self.signer.sign(next_word)

        return next_word
    
    def dispatch(self, request, *args, **kwargs):
        # Set session to request header
        request.session['header'] = 'value'
        return super().dispatch(request, *args, **kwargs)
    
    def get_word_with_start_letter(self, start_letter):
        word = Word.objects.filter(word__startswith=start_letter).order_by('?').first()
        return word.word
    
    def is_sign_valid(self, word):
        sign = self.request.session.get('sign')
        return self.signer.unsign(sign) == word
    
    def is_valid_answer(self, word, answer):
        if not word[-1] == answer[0] or not self.is_sign_valid(word):
            return False
        return Word.objects.filter(word=answer).exists()
    
    def post(self, request, *args, **kwargs):
        word = request.POST.get('word')
        answer = request.POST.get('answer')
        if self.is_valid_answer(word, answer):
            word_validated = answer
            messages.success(request, 'Correct!')
        else:
            word_validated = None
            messages.error(request, 'Incorrect!')

        next_word = self.get_randoms_word(word_validated)

        return self.render_to_response({'word': next_word})