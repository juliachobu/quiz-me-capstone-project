from django.db import models
from django.urls import reverse
from quiz_project.settings import AUTH_USER_MODEL

class quizQuestions(models.Model):
    question = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)



    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse("", args=(self.pk,))
        
