from django.db import models
from django.contrib.auth.models import User
import datetime

class QuestionManager(models.Manager):
    def new(self):
        return Question.objects.all().order_by('added_at')
    def popular(self):
        return Question.objects.all().order_by('-rating')

class Question(models.Model):
    objects=QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User,related_name='question_like_user')
    def get_url(self):
        return '/question/' + str(self.id)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.OneToOneField(Question)
    author = models.ForeignKey(User)
