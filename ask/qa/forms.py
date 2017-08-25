from django import forms
from .models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(min_length = 1, max_length = 255)
    text = forms.CharField(min_length=1,widget=forms.Textarea)
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(min_length=1,widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError('Question not found')
        return question
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
