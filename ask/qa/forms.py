from django import forms
from .models import Question, Answer
from django.contrib import auth
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

class LoginForm(forms.Form):
    username = forms.CharField(min_length=1)
    password = forms.CharField(min_length=1,widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError('Authorization failed')
        self.cleaned_data['user'] = user
        return self.cleaned_data
    def save(self):
        return self.cleaned_data['user']

class RegisterForm(LoginForm):
    email = forms.EmailField()
    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            auth.models.User.objects.get(username=username)
        except auth.models.User.DoesNotExist:
            return username
        raise forms.ValidationError('Username already used')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            auth.models.User.objects.get(email=email)
        except auth.models.User.DoesNotExist:
            return email
        raise forms.ValidationError('Email already used')
    def clean(self):
        if self._errors:
            raise forms.ValidationError('Registration failed')
        auth.models.User.objects.create_user(**self.cleaned_data)
        return super(RegisterForm,self).clean()
