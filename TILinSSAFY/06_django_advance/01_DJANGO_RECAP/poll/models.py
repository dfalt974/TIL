from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)

class Choice(models.Model):
    content = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
