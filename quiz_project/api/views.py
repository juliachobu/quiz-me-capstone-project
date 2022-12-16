from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics


from quiz_me_app.models import Question, Choice, Result
from .serializers import QuestionSerializer, ChoiceSerializer, ResultSerializer, UserSerializer




class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
   

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        print(self.request.user)
        return self.request.user