from django.db import models

from quiz_project.settings import AUTH_USER_MODEL

class Question(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

    

class Choice(models.Model):
    text = models.CharField(max_length=200)  
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE)  
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text


class Result(models.Model):
    correct_answer = models.BooleanField(default=False)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='results', on_delete=models.CASCADE)

    def __str__(self):
       return self.question.text